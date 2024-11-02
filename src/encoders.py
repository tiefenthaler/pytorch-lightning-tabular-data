from typing import Any, Callable, Dict, Iterable, List, Tuple, Union
import warnings

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin, OneToOneFeatureMixin
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
import torch

# Custom transformer to use attributes from the OrdinalEncoder
class OrdinalEncoderExtensionUnknowns(BaseEstimator, TransformerMixin, OneToOneFeatureMixin):

    def _transform_unknown_values(self, X):
        """Generalized function to transform encoded values."""
        return np.where(X == -1, 0, X + 1)
    
    def _inverse_transform_unknown_values(self, X):
        """Generalized function to inverse transform values."""
        return np.where(X == 0, -1, X - 1)
    
    def fit(self, X, y=None):
        # Fit the OrdinalEncoderExtension
        return self
    
    def transform(self, X):
        # Handle different input types
        if isinstance(X, np.ndarray):
            X_transformed = self._transform_unknown_values(X)
        elif isinstance(X, pd.Series):
            X_transformed = X.copy()
            X_transformed = self._transform_unknown_values(X_transformed)
            X_transformed = pd.Series(X_transformed, index=X.index, name=X.name)
        elif isinstance(X, pd.DataFrame):
            X_transformed = X.copy()
            # Apply transformation to each column
            X_transformed = X_transformed.apply(self._transform_unknown_values)
        else:
            raise ValueError("Input must be a pandas DataFrame, Series, or NumPy array")

        return X_transformed

    def inverse_transform(self, X):
        # Handle different input types for inverse transformation
        if isinstance(X, np.ndarray):
            X_inverse = self._inverse_transform_unknown_values(X)
        elif isinstance(X, pd.Series):
            X_inverse = X.copy()
            X_inverse = self._inverse_transform_unknown_values(X_inverse)
            X_inverse = pd.Series(X_inverse, index=X.index, name=X.name)
        elif isinstance(X, pd.DataFrame):
            X_inverse = X.copy()
            # Apply inverse transformation to each column
            X_inverse = X_inverse.apply(self._inverse_transform_unknown_values)

        return X_inverse
    
    def get_feature_names_out(self, *args, **params):
        return self.columns_



# Example usage
if __name__ == "__main__":
    # Sample data as DataFrame
    data_df = pd.DataFrame({
        'category': ['a', 'b', 'c', 'a'],
        'category2': ['1', '3', '5', '3']
    })

    test_df = pd.DataFrame({
        'category': ['a', 'b', 'c', 'a', 'unknown'],
        'category2': ['1', '3', '5', '3', '999']
    })
    
    # Create the pipeline for DataFrame
    pipeline_df = Pipeline(steps=[
        ('ordinal_encoder', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)),
        ('custom_transformer', OrdinalEncoderExtensionUnknowns())
    ])
    
    # Fit and transform the DataFrame
    transformed_df = pipeline_df.fit_transform(data_df)
    print("Transformed DataFrame:")
    print(transformed_df)

    # Transform the DataFrame
    transformed_df = pipeline_df.transform(test_df)
    print("\nTransformed DataFrame:")
    print(transformed_df)

    # Inverse transform the DataFrame
    inverse_df = pipeline_df.named_steps['custom_transformer'].inverse_transform(transformed_df)
    print("\nInverse Transformed DataFrame:")
    print(inverse_df)