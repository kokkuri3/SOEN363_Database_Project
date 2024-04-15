import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient, ASCENDING
import threading

# Replace the connection string with your own MongoDB Atlas connection string
uri = 'mongodb+srv://soen363prjoect2:fQqnbq4VU7LxmAO6@cluster0.y4umf8o.mongodb.net/'

class MongoQueryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MongoDB Query App")

        # MongoDB Connection
        self.client = MongoClient(uri)
        self.database = self.client.get_database('soen363p2')

        # Collection dropdown
        self.collection_var = tk.StringVar()
        self.collection_label = ttk.Label(root, text="Collection:")
        self.collection_label.grid(row=0, column=0, padx=10, pady=5)
        self.collection_dropdown = ttk.Combobox(root, textvariable=self.collection_var)
        self.collection_dropdown['values'] = ['Car', 'Customer', 'Employee', 'Reservation', 'Review', 'User']
        self.collection_dropdown.grid(row=0, column=1, padx=10, pady=5)
        self.collection_dropdown.current(0)

        # Query dropdown
        self.query_var = tk.IntVar()
        self.query_label = ttk.Label(root, text="Query:")
        self.query_label.grid(row=1, column=0, padx=10, pady=5)
        self.query_dropdown = ttk.Combobox(root, textvariable=self.query_var)
        self.query_dropdown['values'] = [0, 1, 2, 3, 4, 5, 6]
        self.query_dropdown.grid(row=1, column=1, padx=10, pady=5)
        self.query_dropdown.current(0)
        self.query_dropdown.bind("<<ComboboxSelected>>", self.handle_query_selection)

        # Query text input
        self.query_text_label = ttk.Label(root, text="Query Text:")
        self.query_text_label.grid(row=2, column=0, padx=10, pady=5)
        self.query_text_entry = ttk.Entry(root)
        self.query_text_entry.grid(row=2, column=1, padx=10, pady=5)

        # Run button
        self.run_button = ttk.Button(root, text="Run", command=self.run_query)
        self.run_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Result text
        self.result_text = tk.Text(root, height=45, width=200)  # Adjust height and width as needed
        self.result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Hide query text input initially
        self.hide_query_text_input()

    def handle_query_selection(self, event):
        selected_query = self.query_var.get()
        if selected_query == 6:
            self.show_query_text_input()
        else:
            self.hide_query_text_input()

    def show_query_text_input(self):
        self.query_text_label.grid(row=2, column=0, padx=10, pady=5)
        self.query_text_entry.grid(row=2, column=1, padx=10, pady=5)

    def hide_query_text_input(self):
        self.query_text_label.grid_remove()
        self.query_text_entry.grid_remove()

    def run_query(self):
        # Create a new thread for each query execution
        query_thread = threading.Thread(target=self.execute_query)
        query_thread.start()

    def execute_query(self):
        collection_name = self.collection_var.get()
        query_number = self.query_var.get()

        collection = self.database.get_collection(collection_name)
        self.result_text.delete(1.0, tk.END)

        # Display a message indicating that the query is executing
        executing_message = f"Executing query {query_number} for collection: {collection_name}...\n"
        self.result_text.insert(tk.END, executing_message)

        if query_number == 1:
            # Q1 - Basic search query on an attribute value
            collection_criteria = {
                'Car': {"year": 1998},
                'Customer': {"premium": 1},  # Example criteria for Customer collection
                'Employee': {"position": "Salesperson"},  # Example criteria for Employee collection
                'Reservation': {"customer_id": 432095},  # Example criteria for Reservation collection
                'Review': {"rating": {"$gte": 4.1}},  # Example criteria for Review collection
                'User': {"name": "Steven Hanson"}  # Example criteria for User collection
            }

            # Get the criteria for the selected collection
            basic_query = collection_criteria.get(collection_name, {})
            # Display the collection criteria
            self.result_text.insert(tk.END, f"Collection Criteria: {basic_query}\n\n")
            # Execute the query and display the results
            basic_result = list(collection.find(basic_query))
            self.display_result(basic_result)
            self.result_text.insert(tk.END, f"\n\n -- End of Query --")

        elif query_number == 2:
            # Q2 - Query providing aggregate data for a specific criteria
            collection_criteria = {
                'Car': {"year": 1998},
                'Customer': {"premium": 1},  # Example criteria for Customer collection
                'Employee': {"position": "Salesperson"},  # Example criteria for Employee collection
                'Reservation': {"customer_id": 432095},  # Example criteria for Reservation collection
                'Review': {"rating": {"$gte": 4.1}},  # Example criteria for Review collection
                'User': {"name": "Steven Hanson"}  # Example criteria for User collection
            }

            # Get the criteria for the selected collection
            criteria = collection_criteria.get(collection_name, {})

            aggregate_query = [
                {"$match": criteria},  # Match stage to filter results based on criteria
                {"$group": {"_id": None, "sum": {"$sum": 1}}}  # Group stage for aggregation
            ]
            aggregate_result = list(collection.aggregate(aggregate_query))

            # Display the criteria used in the output
            self.result_text.insert(tk.END, f"Criteria used: {criteria}\n")

            # Display the sum of items that satisfy the query
            if aggregate_result:
                sum_of_items = aggregate_result[0].get('sum', 0)
                self.result_text.insert(tk.END, f"Sum of items: {sum_of_items}\n")
            else:
                self.result_text.insert(tk.END, "No items found.\n")
            self.result_text.insert(tk.END, f"\n\n -- End of Query --")

        elif query_number == 3:
            # Q3 - Find top 5 entities satisfying a criteria, sorted by an attribute
            TO_DO = ''
            self.result_text.insert(tk.END, f"\n\n -- End of Query --")

        elif query_number == 4:
            # Q4 - Simulate a relational group by query in NoSQL (aggregate per category)
            # This query is mostly done for Cars, but the TotalAmount will work on every table
            pipeline = [
                {
                    "$group": {
                    "_id": "$category",
                    "TotalAmount" : { "$sum": 1 }, 
                    "mpgAvg": { "$avg": "$mpg" }, 
                    "horsepowerAvg": { "$avg": "$horsepower" }
                    }                   
                }
            ]

            results = list(collection.aggregate(pipeline))
            
            self.display_result(results)
            self.result_text.insert(tk.END, f"\n\n -- End of Query --")
            

        elif query_number == 5:
            # Q5 - Build appropriate indexes
            index_name = f"{collection_name.lower()}_index"
            index_statement = collection.create_index([("_id", ASCENDING)])
            self.result_text.insert(tk.END, f"-- Index Creation Statement --\n")
            self.result_text.insert(tk.END, f"Index Name: {index_name}\n")
            self.result_text.insert(tk.END, f"Field(s): _id\n")
            self.result_text.insert(tk.END, f"Type: Ascending\n\n")

            # Query execution time before creating index
            before_index_time = collection.find({}).explain()["executionStats"]["executionTimeMillis"]

            # Execute a dummy query after creating index
            dummy_query_result = list(collection.find({}))

            # Report query execution time before and after creating index
            after_index_time = collection.find({}).explain()["executionStats"]["executionTimeMillis"]
            self.result_text.insert(tk.END, f"Query Execution Time Before Creating Index: {before_index_time} ms\n")
            self.result_text.insert(tk.END, f"Query Execution Time After Creating Index: {after_index_time} ms\n")
            self.result_text.insert(tk.END, f"\n\n -- End of Query --")

        elif query_number == 6:
            # Q6 - Demonstrate a full text search
            search_text = self.query_text_entry.get()
            # Escape double quotation marks
            escaped_search_text = search_text.replace('"', '\\"')

            # Check if the input can be converted to an integer
            try:
                integer_search_value = int(escaped_search_text)
                # Display message if the input is a number
                self.result_text.insert(tk.END, "Numbers are not supported in text search.\n")
                self.result_text.insert(tk.END, f"\n\n -- End of Query --")
                return
            except ValueError:
                pass  # Continue if the input is not a number

            # Construct a query for text search
            text_query = {"$text": {"$search": f'"{escaped_search_text}"'}}

           # Perform the text search
        full_text_result = collection.find(text_query)

        # Display results if any, or indicate no results found
        found_results = False
        for result in full_text_result:
            found_results = True
            self.display_result([result])

        if not found_results:
            self.result_text.insert(tk.END, "No results found.\n")

            self.result_text.insert(tk.END, f"\n\n -- End of Query --")

        elif query_number == 0:
            # Q0 - List all items in the collection
            all_items_query = collection.find({})
            all_items_result = list(all_items_query)
    
            # Display the total number of results
            total_results = len(all_items_result)
            self.result_text.insert(tk.END, f"Total Results: {total_results}\n\n")
    
            # Display all items
            self.display_result(all_items_result)
            self.result_text.insert(tk.END, f"\n\n -- End of Query --")


    def display_result(self, result):
        # Display results
        for doc in result:
            doc.pop('_id', None)  # Remove '_id' field
            self.result_text.insert(tk.END, f"{doc}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = MongoQueryApp(root)
    root.mainloop()
