CREATE INDEX IF NOT EXISTS idx_products_updated_id
ON products(updated_at DESC, id DESC);

CREATE INDEX IF NOT EXISTS idx_products_category_updated_id
ON products(category, updated_at DESC, id DESC);