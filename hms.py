import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Hospital Management System")

    def open_doctor_department():
        root.destroy()
        doctor_department_window()

    def open_patient_department():
        root.destroy()
        patient_department_window()

    def exit_program():
        root.quit()

    main_label = tk.Label(root, text="Welcome to Hospital Management System", font=("Helvetica", 16))
    main_label.pack(pady=20)

    doctor_button = tk.Button(root, text="Doctor Department", command=open_doctor_department)
    doctor_button.pack(pady=5)

    patient_button = tk.Button(root, text="Patient Department", command=open_patient_department)
    patient_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=exit_program)
    exit_button.pack(pady=5)

    root.mainloop()

def doctor_department_window():
    def writeD():
        write_window = tk.Toplevel()
        write_window.title("Add New Doctor Record")

        id_var = tk.StringVar()
        name_var = tk.StringVar()
        age_var = tk.StringVar()
        mobile_var = tk.StringVar()
        department_var = tk.StringVar()
        salary_var = tk.StringVar()

        def save_record():
            id = id_var.get()
            name = name_var.get()
            age = age_var.get()
            mobile = mobile_var.get()
            department = department_var.get()
            salary = salary_var.get()

            with open('DoctorPy.txt', 'a') as file:
                file.write(f"{id}\t\t{name}\t\t{age}\t\t{mobile}\t\t{department}\t\t{salary}\n")

            status_label.config(text="Record saved successfully!")

        id_label = tk.Label(write_window, text="Doctor ID:")
        id_label.grid(row=0, column=0)
        id_entry = tk.Entry(write_window, textvariable=id_var)
        id_entry.grid(row=0, column=1)

        name_label = tk.Label(write_window, text="Doctor Name:")
        name_label.grid(row=1, column=0)
        name_entry = tk.Entry(write_window, textvariable=name_var)
        name_entry.grid(row=1, column=1)

        age_label = tk.Label(write_window, text="Doctor Age:")
        age_label.grid(row=2, column=0)
        age_entry = tk.Entry(write_window, textvariable=age_var)
        age_entry.grid(row=2, column=1)

        mobile_label = tk.Label(write_window, text="Doctor Mobile:")
        mobile_label.grid(row=3, column=0)
        mobile_entry = tk.Entry(write_window, textvariable=mobile_var)
        mobile_entry.grid(row=3, column=1)

        department_label = tk.Label(write_window, text="Doctor Department:")
        department_label.grid(row=4, column=0)
        department_entry = tk.Entry(write_window, textvariable=department_var)
        department_entry.grid(row=4, column=1)

        salary_label = tk.Label(write_window, text="Doctor Salary:")
        salary_label.grid(row=5, column=0)
        salary_entry = tk.Entry(write_window, textvariable=salary_var)
        salary_entry.grid(row=5, column=1)

        save_button = tk.Button(write_window, text="Save Record", command=save_record)
        save_button.grid(row=6, column=0, columnspan=2)

        status_label = tk.Label(write_window, text="")
        status_label.grid(row=7, column=0, columnspan=2)

    doctor_window = tk.Toplevel()
    doctor_window.title("Doctor Department")

    add_button = tk.Button(doctor_window, text="Add New Doctor Record", command=writeD)
    add_button.pack(pady=10)

    back_button = tk.Button(doctor_window, text="Back to Main Menu", command=main)
    back_button.pack(pady=10)

def patient_department_window():
    def writeP():
        write_window = tk.Toplevel()
        write_window.title("Add New Patient Record")

        id_var = tk.StringVar()
        name_var = tk.StringVar()
        age_var = tk.StringVar()
        mobile_var = tk.StringVar()
        disease_var = tk.StringVar()
        treatment_var = tk.StringVar()

        def save_record():
            id = id_var.get()
            name = name_var.get()
            age = age_var.get()
            mobile = mobile_var.get()
            disease = disease_var.get()
            treatment = treatment_var.get()

            with open('PatientPy.txt', 'a') as file:
                file.write(f"{id}\t\t{name}\t\t{age}\t\t{mobile}\t\t{disease}\t\t{treatment}\n")

            status_label.config(text="Record saved successfully!")

        id_label = tk.Label(write_window, text="Patient ID:")
        id_label.grid(row=0, column=0)
        id_entry = tk.Entry(write_window, textvariable=id_var)
        id_entry.grid(row=0, column=1)

        name_label = tk.Label(write_window, text="Patient Name:")
        name_label.grid(row=1, column=0)
        name_entry = tk.Entry(write_window, textvariable=name_var)
        name_entry.grid(row=1, column=1)

        age_label = tk.Label(write_window, text="Patient Age:")
        age_label.grid(row=2, column=0)
        age_entry = tk.Entry(write_window, textvariable=age_var)
        age_entry.grid(row=2, column=1)

        mobile_label = tk.Label(write_window, text="Patient Mobile:")
        mobile_label.grid(row=3, column=0)
        mobile_entry = tk.Entry(write_window, textvariable=mobile_var)
        mobile_entry.grid(row=3, column=1)

        disease_label = tk.Label(write_window, text="Patient Disease:")
        disease_label.grid(row=4, column=0)
        disease_entry = tk.Entry(write_window, textvariable=disease_var)
        disease_entry.grid(row=4, column=1)

        treatment_label = tk.Label(write_window, text="Treatment:")
        treatment_label.grid(row=5, column=0)
        treatment_entry = tk.Entry(write_window, textvariable=treatment_var)
        treatment_entry.grid(row=5, column=1)

        save_button = tk.Button(write_window, text="Save Record", command=save_record)
        save_button.grid(row=6, column=0, columnspan=2)

        status_label = tk.Label(write_window, text="")
        status_label.grid(row=7, column=0, columnspan=2)

    patient_window = tk.Toplevel()
    patient_window.title("Patient Department")

    add_button = tk.Button(patient_window, text="Add New Patient Record", command=writeP)
    add_button.pack(pady=10)

    back_button = tk.Button(patient_window, text="Back to Main Menu", command=main)
    back_button.pack(pady=10)

main()