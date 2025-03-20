import streamlit as st
import json

# Load and save files
def load_file():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library():
    with open("library.json", "w") as file:
        return json.dump(library, file, indent=4)

# Initialize library
library = load_file()

st.title("📚 Personal Library Manager")
menu = st.sidebar.radio("Select an option", ["📖 View Library", "➕ Add Books", "❌ Remove Book", "🔍 Search Book", "💾 Save and Exit"])

if menu == "📖 View Library":
    st.sidebar.write("📚 Your Library")  # Emoji added
    if library:
        st.table(library)
    else:
        st.write("📭 No books found")  # Emoji added

# Add book
elif menu == "➕ Add Books":
    st.sidebar.write("📖 Add a New Book")  # Emoji added
    title = st.text_input("📝 Title")  # Emoji added
    author = st.text_input("👤 Author")  # Emoji added
    year = st.number_input("📅 Year", min_value=2022, max_value=2100, step=1)  # Emoji added
    genre = st.text_input("🎭 Genre")  # Emoji added
    read_status = st.checkbox("✅ Mark as Read")  # Emoji added

    if st.button("➕ Add Book"):  # Emoji added
        library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
        save_library()
        st.success("🎉 Book added successfully!")  # Emoji added
        st.rerun()

# Remove book
elif menu == "❌ Remove Book":
    st.sidebar.write("❌ Remove a Book")  # Emoji added
    book_title = [book["title"] for book in library]

    if book_title:
        selected_book = st.selectbox("📚 Select a book to remove", book_title)  # Emoji added
        if st.button("❌ Remove Book"):  # Emoji added
            library = [book for book in library if book["title"] != selected_book]
            save_library()
            st.success("🗑️ Book successfully removed!")  # Emoji added
            st.rerun()
    else:
        st.warning("📭 No books in your library. Add some books!")  # Emoji added

# Search book
elif menu == "🔍 Search Book":
    st.sidebar.write("🔍 Search a Book")  # Emoji added
    search_term = st.text_input("🔎 Enter title or author name")  # Emoji added
    if st.button("🔍 Search"):  # Emoji added
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("📭 No books found!")  # Emoji added

# Save and exit
elif menu == "💾 Save and Exit":
    save_library()
    st.success("💾 Library saved successfully!")  # Emoji added