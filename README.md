# Users API Documentation

Base URL:  
`http://127.0.0.1:8000/api/users/`

---

## Signup

Create a new user account.

- **Method:** POST  
- **Endpoint:** `/signup/`  
- **Authentication:** None  
- **Content-Type:** `application/json`

### Request Body:

{
"fullname": "John Doe",
"email": "john@example.com",
"password": "StrongPassword123"
}


### Response:

- 201 Created with user data (except password)

---

## Login (Obtain JWT tokens)

Authenticate user and receive access and refresh tokens.

- **Method:** POST  
- **Endpoint:** `/login/`  
- **Authentication:** None  
- **Content-Type:** `application/json`

### Request Body:

{
"email": "john@example.com",
"password": "StrongPassword123"
}


### Response:

{
"refresh": "<refresh_token>",
"access": "<access_token>",
"fullname": "John Doe" // custom claim added
}


---

## Refresh Token

Get new access token using refresh token.

- **Method:** POST  
- **Endpoint:** `/login/refresh/`  
- **Authentication:** None  
- **Content-Type:** `application/json`

### Request Body:

{
"refresh": "<refresh_token>"
}


### Response:

{
"access": "<new_access_token>"
}


---

## View Profile

Get the profile details of the logged-in user.

- **Method:** GET  
- **Endpoint:** `/profile/`  
- **Authentication:** Bearer Token required  
- **Content-Type:** N/A

### Response:

{
"access": "<new_access_token>"
}


---

## View Profile

Get the profile details of the logged-in user.

- **Method:** GET  
- **Endpoint:** `/profile/`  
- **Authentication:** Bearer Token required  
- **Content-Type:** N/A

### Response:

{
"id": 1,
"fullname": "John Doe",
"email": "john@example.com",
"profile_image": "http://127.0.0.1:8000/media/profiles/john.jpg",
"phone_number": "1234567890",
"address_line": "123 Main Street",
"pincode": "123456",
"nearest_area": "Downtown"
}


---

## Update Profile

Update profile information of logged-in user.

- **Method:** PUT or PATCH  
- **Endpoint:** `/profile/update/`  
- **Authentication:** Bearer Token required  
- **Content-Type:** `multipart/form-data` (for file upload) or `application/json`

### Form-data or JSON example:

| Key           | Type  | Description               |
|---------------|-------|---------------------------|
| fullname      | Text  | Full name                 |
| profile_image | File  | Profile image file (optional) |
| phone_number  | Text  | Phone number              |
| address_line  | Text  | Address                   |
| pincode      | Text   | Postal code               |
| nearest_area | Text   | Nearest area/locality     |

---

## Logout (If implemented)

- **Method:** POST  
- **Endpoint:** `/logout/`  
- **Authentication:** Bearer Token required  
- **Content-Type:** `application/json`

### Request Body:

{
"refresh": "<refresh_token>"
}


### Response:

{
"detail": "Successfully logged out."
}


---

# Notes

- Use `Authorization: Bearer <access_token>` header for all protected endpoints.
- Passwords must respect Django’s password validation rules.
- Profile image uploads need `multipart/form-data`.
- Login returns JWT tokens with a custom `fullname` claim for user convenience.
- Refresh tokens should be securely stored client-side and used to obtain new access tokens.














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


