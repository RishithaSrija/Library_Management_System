from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class Library:
    def add_member(self, name, email):
        existing = supabase.table("members").select("*").eq("email", email).execute()
        if existing.data:
            print(f"Member with email {email} already exists.")
            return
        supabase.table("members").insert({"name": name, "email": email}).execute()
        print(f"Member '{name}' ({email}) added successfully.")

    def add_book(self, title, author, category, stock):
        supabase.table("books").insert({
            "title": title,
            "author": author,
            "category": category,
            "stock": stock
        }).execute()
        print(f"Book '{title}' added successfully.")

    def list_books(self):
        res = supabase.table("books").select("*").execute()
        print("\nBooks available:")
        for b in res.data:
            print(f"[{b['book_id']}] '{b['title']}' by {b['author']} - Category: {b['category']}, Stock: {b['stock']}")

    def search_books(self, keyword):
        res = supabase.table("books").select("*").ilike("title", f"%{keyword}%").execute()
        res_author = supabase.table("books").select("*").ilike("author", f"%{keyword}%").execute()
        res_category = supabase.table("books").select("*").ilike("category", f"%{keyword}%").execute()
        data = res.data + res_author.data + res_category.data
        data = {d['book_id']: d for d in data}.values()
        if not data:
            print("No books found.")
            return
        print("\nSearch results:")
        for b in data:
            print(f"[{b['book_id']}] '{b['title']}' by {b['author']} - Category: {b['category']}, Stock: {b['stock']}")

    def list_members(self):
        res = supabase.table("members").select("*").execute()
        print("\nLibrary Members:")
        for m in res.data:
            print(f"[{m['member_id']}] {m['name']} - Email: {m['email']}")

    def update_member_email(self, member_id, new_email):
        supabase.table("members").update({"email": new_email}).eq("member_id", member_id).execute()
        print(f"Member {member_id} email updated to {new_email}")

    def update_book_stock(self, book_id, new_stock):
        supabase.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
        print(f"Book {book_id} stock updated to {new_stock}")

    def delete_member(self, member_id):
        supabase.table("members").delete().eq("member_id", member_id).execute()
        print(f"Member {member_id} deleted successfully")

    def delete_book(self, book_id):
        supabase.table("books").delete().eq("book_id", book_id).execute()
        print(f"Book {book_id} deleted successfully")

    def borrow_book(self, member_id, book_id):
        member_res = supabase.table("members").select("*").eq("member_id", member_id).execute()
        if not member_res.data:
            print("Member not found.")
            return
        member = member_res.data[0]
        book_res = supabase.table("books").select("*").eq("book_id", book_id).execute()
        if not book_res.data:
            print("Book not found.")
            return
        book = book_res.data[0]
        if book["stock"] <= 0:
            print(f"Book '{book['title']}' is not available.")
            return
        supabase.table("books").update({"stock": book["stock"] - 1}).eq("book_id", book_id).execute()
        supabase.table("borrow_records").insert({
            "member_id": member_id,
            "book_id": book_id
        }).execute()
        print(f"Member '{member['name']}' borrowed book '{book['title']}' successfully.")

    def return_book(self, member_id, book_id):
        record_res = supabase.table("borrow_records") \
            .select("*") \
            .eq("member_id", member_id) \
            .eq("book_id", book_id) \
            .is_("return_date", None) \
            .execute()
        if not record_res.data:
            print("No borrow record found for this member and book.")
            return
        record = record_res.data[0]
        book_res = supabase.table("books").select("*").eq("book_id", book_id).execute()
        book = book_res.data[0]
        supabase.table("books").update({"stock": book["stock"] + 1}).eq("book_id", book_id).execute()
        supabase.table("borrow_records").update({
            "return_date": "now()"
        }).eq("record_id", record["record_id"]).execute()
        print(f"Member '{member_id}' returned book '{book['title']}' successfully.")
