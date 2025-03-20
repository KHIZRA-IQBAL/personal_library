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
    st.sidebar.write("📚 Your Library") 
    if library:
        st.table(library)
    else:
        st.write("📭 No books found")  

# Add book
elif menu == "➕ Add Books":
    st.sidebar.write("📖 Add a New Book")  
    title = st.text_input("📝 Title")  
    author = st.text_input("👤 Author")  
    year = st.number_input("📅 Year", min_value=2022, max_value=2100, step=1)  
    genre = st.text_input("🎭 Genre")  
    read_status = st.checkbox("✅ Mark as Read")  

    if st.button("➕ Add Book"): 
        library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
        save_library()
        st.success("🎉 Book added successfully!")  
        st.rerun()

# Remove book
elif menu == "❌ Remove Book":
    st.sidebar.write("❌ Remove a Book")  
    book_title = [book["title"] for book in library]

    if book_title:
        selected_book = st.selectbox("📚 Select a book to remove", book_title)  
        if st.button("❌ Remove Book"): 
            library = [book for book in library if book["title"] != selected_book]
            save_library()
            st.success("🗑️ Book successfully removed!")  
            st.rerun()
    else:
        st.warning("📭 No books in your library. Add some books!")  

# Search book
elif menu == "🔍 Search Book":
    st.sidebar.write("🔍 Search a Book")  
    search_term = st.text_input("🔎 Enter title or author name")  
    if st.button("🔍 Search"):  
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("📭 No books found!")  

# Save and exit
elif menu == "💾 Save and Exit":
    save_library()
    st.success("💾 Library saved successfully!")  