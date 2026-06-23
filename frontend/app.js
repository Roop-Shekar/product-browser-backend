const API_BASE = "http://127.0.0.1:8000";

const tableBody = document.getElementById("productTable");
const totalProducts = document.getElementById("totalProducts");
const loadedCount = document.getElementById("loadedCount");
const categoryFilter = document.getElementById("categoryFilter");

let nextCursor = null;
let snapshot = null;
let loadedProducts = 0;

async function fetchTotalCount() {
    try {
        const res = await fetch(`${API_BASE}/products/count`);
        const data = await res.json();

        totalProducts.textContent = data.total_products;
    } catch (error) {
        console.error("Error loading product count:", error);
    }
}

async function loadProducts(reset = false) {

    if (reset) {
        tableBody.innerHTML = "";
        loadedProducts = 0;
        nextCursor = null;
        snapshot = null;
    }

    let url = `${API_BASE}/products?limit=20`;

    const category = categoryFilter.value;

    if (category) {
        url += `&category=${encodeURIComponent(category)}`;
    }

    if (snapshot) {
        url += `&snapshot=${encodeURIComponent(snapshot)}`;
    }

    if (nextCursor) {
        url += `&cursor_updated_at=${encodeURIComponent(nextCursor.updated_at)}`;
        url += `&cursor_id=${nextCursor.id}`;
    }

    try {
        const res = await fetch(url);
        const data = await res.json();

        if (!snapshot) {
            snapshot = data.snapshot;
        }

        nextCursor = data.next_cursor;

        data.products.forEach(product => {

            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${product.id}</td>
                <td>${product.name}</td>
                <td>${product.category}</td>
                <td>$${product.price}</td>
                <td>${new Date(product.updated_at).toLocaleString()}</td>
            `;

            tableBody.appendChild(row);
        });

        loadedProducts += data.products.length;
        loadedCount.textContent = loadedProducts;

        if (!nextCursor) {
            document.getElementById("loadMoreBtn").disabled = true;
            document.getElementById("loadMoreBtn").textContent = "No More Products";
        }

    } catch (error) {
        console.error("Error loading products:", error);
    }
}

async function loadCategories() {

    try {
        const res = await fetch(`${API_BASE}/products?limit=100`);
        const data = await res.json();

        const categories = [
            ...new Set(
                data.products.map(product => product.category)
            )
        ];

        categories.sort();

        categories.forEach(category => {

            const option = document.createElement("option");

            option.value = category;
            option.textContent = category;

            categoryFilter.appendChild(option);
        });

    } catch (error) {
        console.error("Error loading categories:", error);
    }
}

document
    .getElementById("loadMoreBtn")
    .addEventListener("click", () => {
        loadProducts();
    });

document
    .getElementById("applyFilter")
    .addEventListener("click", () => {

        document.getElementById("loadMoreBtn").disabled = false;
        document.getElementById("loadMoreBtn").textContent = "Load More";

        loadProducts(true);
    });

fetchTotalCount();
loadCategories();
loadProducts();