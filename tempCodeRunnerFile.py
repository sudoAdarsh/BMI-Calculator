# Author: Adarsh Upadhyay

import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("BMI Calculator")
        self.geometry("400x280")

        self.input_section()

    def input_section(self):

        # Adding Frame 
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(fill="both", expand=True, pady=10, padx=10)
        
        # Resizing and scaling
        input_frame.columnconfigure(0, weight=2)
        input_frame.columnconfigure(1, weight=6)
        input_frame.columnconfigure(2, weight=0)

        # Weight Data
        # label
        weight_label = ctk.CTkLabel(input_frame, text="Weight : ", font=("Arial", 18))
        weight_label.grid(row=0, column=0, padx=(10, 15), pady=5, sticky="ew")

        #Input box
        self.weight_entry = ctk.CTkEntry(input_frame, justify="right", font=("Arial", 18))
        self.weight_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # types of weight units
        self.weight_unit = ctk.CTkOptionMenu(input_frame, values=["kg", "lbs"], font=("Arial", 16), width=80)
        self.weight_unit.set("kg")
        self.weight_unit.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        # Height Data

        #label
        height_label = ctk.CTkLabel(input_frame, text="Height : ", font=("Arial", 18))
        height_label.grid(row=1, column=0, padx=(10, 15), pady=5, sticky="ew")

        # Height input
        self.height_entry = ctk.CTkEntry(input_frame, font=("Arial", 18), justify="right")
        self.height_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Input options
        self.height_unit = ctk.CTkOptionMenu(input_frame, font=("Arial", 16), values=["cm", "inches"], width=80)
        self.height_unit.set("cm")
        self.height_unit.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        # Calculate button
        calc_button = ctk.CTkButton(input_frame,text="Calculate", font=("Arial", 18), command=self.calc_bmi)
        calc_button.grid(row=2, column=0 , columnspan=3, pady=(40, 15), padx=10)

        # Result Label
        self.result_label = ctk.CTkLabel(input_frame, text="", font=("Segoe UI", 18, "bold"))
        self.result_label.grid(row=3, column=0, columnspan=3, pady=(20,0))

    # Calculate BMI
    def calc_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            # convert weight to kg if in lbs
            if self.weight_unit.get() == "lbs":
                weight = weight * 0.45359   # 1 lb = 0.45 kg

            # convert height to meters
            if self.height_unit.get() == "cm":
                height = height / 100  # 1m = 100cm
            elif self.height_unit.get() == "inches":
                height = height * 0.0254 # 1 inch = 0.0254 m

            bmi = weight / (height ** 2)
            category = self.bmi_status(bmi)

            self.result_label.configure(text=f"BMI: {bmi:.2f} ({category})")
        
        except ValueError:
            self.result_label.configure(text="Invalid input")

    def bmi_status(self, bmi):
        if bmi < 16:
            return "Severely Underweight"
        elif bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        elif bmi < 35:
            return "Obese"
        else:
            return "Severely Obese"



app = App()
app.mainloop()