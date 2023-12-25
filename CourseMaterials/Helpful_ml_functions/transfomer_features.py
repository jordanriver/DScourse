def main():
    
def get_feature_names(column_transformer):
    """Get feature names from a ColumnTransformer"""
    output_features = []

    for name, transformer, original_features in column_transformer.transformers_:
        if name == 'remainder':  # Skip the 'remainder' transformer, if present
            continue

        if hasattr(transformer, 'get_feature_names_out'):
            # For transformers with a get_feature_names_out method (OneHotEncoder)
            transformer_features = transformer.get_feature_names_out(original_features)
        else:
            # Transformers without get_feature_names_out (SimpleImputer)
            transformer_features = original_features

        output_features.extend(transformer_features)

    return output_features

if __name__ == "__main__":
    main()