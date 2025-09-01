# Shop API Documentation

Base URL:  
`http://127.0.0.1:8000/api/shop/`

---

## Categories

### List Categories

- **Method:** GET  
- **Endpoint:** `/categories/`  
- **Authentication:** None

**Response Example:**

[
{
"id": 1,
"name": "Fruits",
"description": "Fresh fruits",
"image": "http://127.0.0.1:8000/media/categories/fruits.jpg",
"is_featured": true,
"slug": "fruits",
"created_at": "2025-08-29T15:50:15Z",
"updated_at": "2025-08-29T15:50:15Z"
}
]


---

### Create Category

- **Method:** POST  
- **Endpoint:** `/categories/`  
- **Authentication:** Admin only  
- **Content-Type:** `multipart/form-data`

**Form-data Example:**

| Key         | Type   | Description        |
|-------------|--------|--------------------|
| name        | Text   | Category name      |
| description | Text   | Category description |
| is_featured | Text   | true or false      |
| image       | File   | Image file upload  |

---

### Retrieve Category

- **Method:** GET  
- **Endpoint:** `/categories/{id}/`  
- **Authentication:** None

---

### Update Category

- **Method:** PUT  
- **Endpoint:** `/categories/{id}/`  
- **Authentication:** Admin only  
- **Content-Type:** `multipart/form-data`

Form-data same as **Create Category**

---

### Delete Category

- **Method:** DELETE  
- **Endpoint:** `/categories/{id}/`  
- **Authentication:** Admin only

---

## Products

### List Products

- **Method:** GET  
- **Endpoint:** `/products/`  
- **Authentication:** None

---

### Create Product with Images

- **Method:** POST  
- **Endpoint:** `/products/`  
- **Authentication:** Admin only  
- **Content-Type:** `multipart/form-data`

**Form-data Example:**

| Key             | Type   | Description                 |
|-----------------|--------|-----------------------------|
| category        | Text   | Category ID (integer)       |
| name            | Text   | Product name                |
| description     | Text   | Product description         |
| price           | Text   | Product price (decimal)     |
| discount_price  | Text   | Discount price (optional)   |
| is_featured     | Text   | true or false               |
| stock_available | Text   | Stock quantity (integer)    |
| product_images  | File   | Image file (multiple keys allowed for multiple images) |

---

### Retrieve Product

- **Method:** GET  
- **Endpoint:** `/products/{id}/`  
- **Authentication:** None

---

### Update Product with Images

- **Method:** PUT  
- **Endpoint:** `/products/{id}/`  
- **Authentication:** Admin only  
- **Content-Type:** `multipart/form-data`

Pass form-data similar to **Create Product** including optional multiple `product_images` to replace old images.

---

### Delete Product

- **Method:** DELETE  
- **Endpoint:** `/products/{id}/`  
- **Authentication:** Admin only

---

## Ratings

### Add Rating

- **Method:** POST  
- **Endpoint:** `/products/{product_id}/rate/`  
- **Authentication:** User required  
- **Content-Type:** `application/json`

**JSON Example:**

{
"rating": 5,
"review": "Excellent product!"
}


---

### List Ratings

- **Method:** GET  
- **Endpoint:** `/products/{product_id}/ratings/`  
- **Authentication:** None

---

## Cart

### List Cart Items

- **Method:** GET  
- **Endpoint:** `/cart/`  
- **Authentication:** User required

---

### Add to Cart

- **Method:** POST  
- **Endpoint:** `/cart/add/`  
- **Authentication:** User required  
- **Content-Type:** `application/json`

**JSON Example:**

{
"product_id": 3,
"quantity": 2
}


---

### Update Cart Item Quantity

- **Method:** PUT  
- **Endpoint:** `/cart/update/{cart_item_id}/`  
- **Authentication:** User required  
- **Content-Type:** `application/json`

**JSON Example:**

{
"quantity": 3
}


---

### Remove Cart Item

- **Method:** DELETE  
- **Endpoint:** `/cart/remove/{cart_item_id}/`  
- **Authentication:** User required

---

## Orders

### Checkout / Create Order

- **Method:** POST  
- **Endpoint:** `/orders/checkout/`  
- **Authentication:** User required  
- **Content-Type:** `application/json`

**JSON Example:**

{
"cart_items":[4]
}


---

### List Orders

- **Method:** GET  
- **Endpoint:** `/orders/`  
- **Authentication:** User required

---

# Notes

- Use header `Authorization: Bearer <access_token>` for all protected routes.
- Use `multipart/form-data` when uploading images.
- Multiple product images can be uploaded by adding multiple `product_images` fields.
- Ensure proper HTTP methods (GET, POST, PUT, DELETE) as per operation.
- Cart is cleared after successful checkout but orders keep detailed order items permanently.

---

You can save this content as `shop_api_documentation.md` and open in any Markdown editor or viewer.

If you want, I can generate a Postman collection JSON file based on this doc for seamless API testing and share its contents here.
