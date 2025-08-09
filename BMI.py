# Author: Adarsh Upadhyay

import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.title("BMI Calculator")
        self.geometry("400x280")

        # Initialize the input section of the app
        self.input_section()

    def input_section(self):

        # Create a frame to hold all input widgets
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(fill="both", expand=True, pady=10, padx=10)
        
        # Configure columns for responsive layout
        input_frame.columnconfigure(0, weight=2)
        input_frame.columnconfigure(1, weight=6)
        input_frame.columnconfigure(2, weight=0)

        # -------------------------------
        # Weight input components
        # -------------------------------

        # Label for Weight input
        weight_label = ctk.CTkLabel(input_frame, text="Weight : ", font=("Arial", 18))
        weight_label.grid(row=0, column=0, padx=(10, 15), pady=5, sticky="ew")

        # Entry box for user to input weight value
        self.weight_entry = ctk.CTkEntry(input_frame, justify="right", font=("Arial", 18))
        self.weight_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Option menu for selecting weight unit (kg or lbs)
        self.weight_unit = ctk.CTkOptionMenu(
            input_frame, values=["kg", "lbs"], font=("Arial", 16), width=80
        )
        self.weight_unit.set("kg")  # default selection
        self.weight_unit.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        # -------------------------------
        # Height input components
        # -------------------------------

        # Label for Height input
        height_label = ctk.CTkLabel(input_frame, text="Height : ", font=("Arial", 18))
        height_label.grid(row=1, column=0, padx=(10, 15), pady=5, sticky="ew")

        # Entry box for user to input height value
        self.height_entry = ctk.CTkEntry(input_frame, font=("Arial", 18), justify="right")
        self.height_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Option menu for selecting height unit (cm or inches)
        self.height_unit = ctk.CTkOptionMenu(
            input_frame, font=("Arial", 16), values=["cm", "inches"], width=80
        )
        self.height_unit.set("cm")  # default selection
        self.height_unit.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        # -------------------------------
        # Calculate button
        # -------------------------------

        # Button to trigger BMI calculation
        calc_button = ctk.CTkButton(
            input_frame, text="Calculate", font=("Arial", 18), command=self.calc_bmi
        )
        calc_button.grid(row=2, column=0, columnspan=3, pady=(40, 15), padx=10)

        # -------------------------------
        # Result display label
        # -------------------------------

        # Label to display the BMI result and category
        self.result_label = ctk.CTkLabel(
            input_frame, text="", font=("Segoe UI", 18, "bold")
        )
        self.result_label.grid(row=3, column=0, columnspan=3, pady=(20, 0))

    # -------------------------------
    # BMI calculation logic
    # -------------------------------
    def calc_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            # Convert weight to kilograms if input is in pounds
            if self.weight_unit.get() == "lbs":
                weight = weight * 0.45359   # 1 lb = 0.45359 kg

            # Convert height to meters based on selected unit
            if self.height_unit.get() == "cm":
                height = height / 100  # 1 m = 100 cm
            elif self.height_unit.get() == "inches":
                height = height * 0.0254 # 1 inch = 0.0254 m

            # Calculate BMI using metric units
            bmi = weight / (height ** 2)

            # Get BMI category based on calculated value
            category = self.bmi_status(bmi)

            # Display BMI and category in result label
            self.result_label.configure(text=f"BMI: {bmi:.2f} ({category})")
        
        except ValueError:
            # Handle invalid or missing inputs gracefully
            self.result_label.configure(text="Invalid input")

    # -------------------------------
    # Determine BMI category based on value
    # -------------------------------
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


# Run the application
app = App()
app.mainloop()
