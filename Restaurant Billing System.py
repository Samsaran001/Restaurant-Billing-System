import mysql.connector
from tkinter import *
import random
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
import cv2

class Bill_App:
    def __init__(self, root): 
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#2d2d2d")
        self.root.title("Restaurant Billing System")
        
        # Database connection
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="restaurant"
        )
        self.mycursor = self.mydb.cursor()
        
        # Variables initialization
        self._total_all_bill = 0
        self.initialize_variables()
        self.create_widgets()
        
    def initialize_variables(self):
        # Product quantity variables
        self.nutella = IntVar()
        self.noodles = IntVar()
        self.lays = IntVar()
        self.oreo = IntVar()
        self.muffin = IntVar()
        self.silk = IntVar()
        self.namkeen = IntVar()
        self.atta = IntVar()
        self.pasta = IntVar()
        self.rice = IntVar()
        self.oil = IntVar()
        self.sugar = IntVar()
        self.dal = IntVar()
        self.tea = IntVar()
        self.soap = IntVar()
        self.shampoo = IntVar()
        self.lotion = IntVar()
        self.cream = IntVar()
        self.foam = IntVar()
        self.mask = IntVar()
        self.sanitizer = IntVar()

        # Total calculation variables
        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.c_name = StringVar()
        self.bill_no = StringVar()
        self.phone = StringVar()
        
        # Initialize bill number
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

    def create_widgets(self):
        # Title Label
        title = Label(self.root, text="Restaurant Billing System", bd=12, relief=RIDGE, 
                     font=("Arial Black", 20), bg="#3498db", fg="white")
        title.pack(fill=X)

        # Customer Details Frame
        details = LabelFrame(self.root, text="Customer Details", font=("Arial Black", 12),
                            bg="#3498db", fg="white", relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)

        # Customer Details Widgets
        Label(details, text="Customer Name", font=("Arial Black", 14), bg="#3498db").grid(row=0, column=0, padx=15)
        Entry(details, borderwidth=4, width=30, textvariable=self.c_name).grid(row=0, column=1, padx=8)
        
        Label(details, text="Contact No.", font=("Arial Black", 14), bg="#3498db").grid(row=0, column=2, padx=10)
        Entry(details, borderwidth=4, width=30, textvariable=self.phone).grid(row=0, column=3, padx=8)
        
        Label(details, text="Bill No.", font=("Arial Black", 14), bg="#3498db").grid(row=0, column=4, padx=10)
        Entry(details, borderwidth=4, width=30, textvariable=self.bill_no).grid(row=0, column=5, padx=8)

        # Menu Sections
        self.create_menu_sections()
        self.create_bill_area()
        self.create_billing_buttons()

    def create_menu_sections(self):
        # Starter Menu
        snacks = LabelFrame(self.root, text="Starter", font=("Arial Black", 12),
                           bg="#3498db", fg="#FFFFFF", relief=GROOVE, bd=10)
        snacks.place(x=5, y=180, height=380, width=325)
        
        starter_items = [
            ("Samosa", self.nutella),
            ("Paneer Tikka", self.noodles),
            ("Chicken Tikka", self.lays),
            ("Vegetable Pakora", self.oreo),
            ("Papdi Chaat", self.muffin),
            ("Tomato Soup", self.silk),
            ("Masala Papad", self.namkeen)
        ]
        for i, (text, var) in enumerate(starter_items):
            Label(snacks, text=text, font=("Arial Black", 11), bg="#3498db").grid(row=i, column=0, pady=11)
            Entry(snacks, borderwidth=2, width=15, textvariable=var).grid(row=i, column=1, padx=10)

        # Main Course Menu
        main_course = LabelFrame(self.root, text="Main Course", font=("Arial Black", 12),
                                bg="#3498db", fg="#FFFFFF", relief=GROOVE, bd=10)
        main_course.place(x=340, y=180, height=380, width=325)
        
        main_items = [
            ("Butter Chicken", self.atta),
            ("Pasta", self.pasta),
            ("Basmati Rice", self.rice),
            ("Paneer Masala", self.oil),
            ("Palak Paneer", self.sugar),
            ("Daal", self.dal),
            ("Chole Bhuture", self.tea)
        ]
        for i, (text, var) in enumerate(main_items):
            Label(main_course, text=text, font=("Arial Black", 11), bg="#3498db").grid(row=i, column=0, pady=11)
            Entry(main_course, borderwidth=2, width=15, textvariable=var).grid(row=i, column=1, padx=10)

        # Snacks Menu
        hygine = LabelFrame(self.root, text="Snacks", font=("Arial Black", 12),
                           bg="#3498db", fg="#FFFFFF", relief=GROOVE, bd=10)
        hygine.place(x=677, y=180, height=380, width=325)
        
        snack_items = [
            ("Noodles", self.soap),
            ("Aloo Tikki Chaat", self.shampoo),
            ("Dahi Vada", self.lotion),
            ("Pav Bhaji", self.cream),
            ("Bhel Puri", self.foam),
            ("Soup", self.mask),
            ("Pokara", self.sanitizer)
        ]
        for i, (text, var) in enumerate(snack_items):
            Label(hygine, text=text, font=("Arial Black", 11), bg="#3498db").grid(row=i, column=0, pady=11)
            Entry(hygine, borderwidth=2, width=15, textvariable=var).grid(row=i, column=1, padx=10)

    def create_bill_area(self):
        # Bill Area
        bill_frame = Frame(self.root, bd=10, relief=GROOVE, bg="#3498db")
        bill_frame.place(x=1010, y=188, width=330, height=372)
        
        Label(bill_frame, text="Bill Area", font=("Arial Black", 17), bd=7, 
             relief=GROOVE, bg="#3498db").pack(fill=X)
        
        scroll_y = Scrollbar(bill_frame, orient=VERTICAL)
        self.txtarea = Text(bill_frame, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    def create_billing_buttons(self):
        # Billing Summary
        billing_menu = LabelFrame(self.root, text="Billing Summary", font=("Arial Black", 12),
                                 relief=GROOVE, bd=10, bg="#3498db", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)

        # Total Labels and Entries
        labels = [
            ("Total Starter Price", self.total_sna),
            ("Total Main Course Price", self.total_gro),
            ("Total Snacks Price", self.total_hyg)
        ]
        for i, (text, var) in enumerate(labels):
            Label(billing_menu, text=text, font=("Arial Black", 11), bg="#3498db").grid(row=i, column=0)
            Entry(billing_menu, width=30, borderwidth=2, textvariable=var).grid(row=i, column=1, padx=10, pady=7)

        # Tax Labels and Entries
        tax_labels = [
            ("Starter Tax", self.a),
            ("Main Course Tax", self.b),
            ("Snacks Tax", self.c)
        ]
        for i, (text, var) in enumerate(tax_labels):
            Label(billing_menu, text=text, font=("Arial Black", 11), bg="#3498db").grid(row=i, column=2)
            Entry(billing_menu, width=30, borderwidth=2, textvariable=var).grid(row=i, column=3, padx=10, pady=7)

        # Buttons Frame
        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#6ff02f")
        button_frame.place(x=800, width=500, height=95)
        
        buttons = [
            ("Total Bill", self.total_bill),
            ("Clear Field", self.clear_fields),
            ("QR", self.display_qr),
            ("Calculator", self.open_calculator),
            ("CV", self.open_computer_vision),
            ("Exit", self.exit_app)
        ]
        for i, (text, cmd) in enumerate(buttons):
            Button(button_frame, text=text, font=("Arial Black", 10), pady=8,
                  bg="#3498db", fg="#000000", command=cmd).grid(row=0, column=i, padx=8)

    def total_bill(self):
        if not self.c_name.get() or not self.phone.get():
            messagebox.showerror("Error", "Please fill customer details!")
            return

        # Calculate prices
        prices = {
            'snacks': [
                (self.nutella, 120),
                (self.noodles, 40),
                (self.lays, 10),
                (self.oreo, 20),
                (self.muffin, 30),
                (self.silk, 60),
                (self.namkeen, 15)
            ],
            'main_course': [
                (self.atta, 42),
                (self.pasta, 120),
                (self.rice, 160),
                (self.oil, 113),
                (self.sugar, 55),
                (self.dal, 76),
                (self.tea, 480)
            ],
            'snacks2': [
                (self.soap, 30),
                (self.shampoo, 180),
                (self.lotion, 500),
                (self.cream, 130),
                (self.foam, 85),
                (self.mask, 100),
                (self.sanitizer, 20)
            ]
        }

        total_starter = sum(q.get() * p for q, p in prices['snacks'])
        total_main = sum(q.get() * p for q, p in prices['main_course'])
        total_snacks = sum(q.get() * p for q, p in prices['snacks2'])

        # Set totals
        self.total_sna.set(f"{total_starter} Rs")
        self.total_gro.set(f"{total_main} Rs")
        self.total_hyg.set(f"{total_snacks} Rs")

        # Calculate taxes
        tax_starter = total_starter * 0.05
        tax_main = total_main * 0.01
        tax_snacks = total_snacks * 0.10

        self.a.set(f"{round(tax_starter, 2)} Rs")
        self.b.set(f"{round(tax_main, 2)} Rs")
        self.c.set(f"{round(tax_snacks, 2)} Rs")

        # Total amount
        self._total_all_bill = total_starter + total_main + total_snacks + tax_snacks + tax_main + tax_snacks
        self.save_to_database()
        self.update_bill_area()

    def save_to_database(self):
        try:
            self.mycursor.execute("""
                INSERT INTO orders (bill_no, customer_name, phone, starter_total, main_total, snacks_total, total_amount)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                self.bill_no.get(),
                self.c_name.get(),
                self.phone.get(),
                self.total_sna.get(),
                self.total_gro.get(),
                self.total_hyg.get(),
                self._total_all_bill
            ))
            self.mydb.commit()
            messagebox.showinfo("Success", "Order saved successfully!")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def update_bill_area(self):
        self.txtarea.delete(1.0, END)
        self.txtarea.insert(END, "\tWELCOME TO OUR RESTAURANT\n\tPhone: 9876543210\n")
        self.txtarea.insert(END, f"\nBill No: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone No: {self.phone.get()}")
        self.txtarea.insert(END, "\n==================================\n")
        self.txtarea.insert(END, "Item\t\tQty\tPrice\n")
        self.txtarea.insert(END, "\n==================================\n")

        # Add items dynamically
        items = [
            ("Samosa", self.nutella, 120),
            ("Paneer Tikka", self.noodles, 40),
            ("Chicken Tikka", self.lays, 10),
            ("Vegetable Pakora", self.oreo, 20),
            ("Papdi Chaat", self.muffin, 30),
            ("Tomato Soup", self.silk, 60),
            ("Masala Papad", self.namkeen, 15),
            ("Butter Chicken", self.atta, 42),
            ("Pasta", self.pasta, 120),
            ("Basmati Rice", self.rice, 160),
            ("Paneer Masala", self.oil, 113),
            ("Palak Paneer", self.sugar, 55),
            ("Daal", self.dal, 76),
            ("Chole Bhuture", self.tea, 480),
            ("Noodles", self.soap, 30),
            ("Aloo Tikki Chaat", self.shampoo, 180),
            ("Dahi Vada", self.lotion, 500),
            ("Pav Bhaji", self.cream, 130),
            ("Bhel Puri", self.foam, 85),
            ("Soup", self.mask, 100),
            ("Pokara", self.sanitizer, 20)
        ]

        for item in items:
            qty = item[1].get()
            if qty > 0:
                self.txtarea.insert(END, f"{item[0]}\t\t{qty}\t{qty * item[2]}\n")

        self.txtarea.insert(END, "\n----------------------------------\n")
        self.txtarea.insert(END, f"Total Amount: {round(self._total_all_bill, 2)} Rs\n")
        self.txtarea.insert(END, "==================================\n")

    def clear_fields(self):
        # Reset all input fields
        for var in [self.nutella, self.noodles, self.lays, self.oreo, self.muffin,
                   self.silk, self.namkeen, self.atta, self.pasta, self.rice,
                   self.oil, self.sugar, self.dal, self.tea, self.soap,
                   self.shampoo, self.lotion, self.cream, self.foam, self.mask,
                   self.sanitizer]:
            var.set(0)
            
        self.total_sna.set("")
        self.total_gro.set("")
        self.total_hyg.set("")
        self.a.set("")
        self.b.set("")
        self.c.set("")
        self.c_name.set("")
        self.phone.set("")
        self.txtarea.delete(1.0, END)
        self.bill_no.set(str(random.randint(1000, 9999)))

    def display_qr(self):
        data = f"Bill No: {self.bill_no.get()}\nCustomer: {self.c_name.get()}\nTotal: {round(self._total_all_bill, 2)} Rs"
        qr = qrcode.QRCode(version=1, box_size=5, border=2)
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img = ImageTk.PhotoImage(img)
        
        qr_window = Toplevel()
        qr_window.title("QR Code")
        Label(qr_window, image=img).pack()
        
        # Close button
        Button(qr_window, text="Close", command=qr_window.destroy).pack(pady=5)
        
        # Close on Escape key
        qr_window.bind("<Escape>", lambda e: qr_window.destroy())
        qr_window.image = img  # Keep reference
    def open_calculator(self):
        try:
            import os
            if os.name == "nt":  # For Windows
                os.system("calc")
            elif os.name == "posix":  # For Linux/MacOS
                os.system("gnome-calculator")  # or "xcalc" depending on the system
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open calculator: {str(e)}")
    def open_computer_vision(self):
        cap = cv2.VideoCapture(0)  # Open webcam
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Computer Vision", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
                break
        cap.release()
        cv2.destroyAllWindows()    

    def exit_app(self):
        self.mydb.close()
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = Bill_App(root)
    root.mainloop()