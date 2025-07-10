import numpy as np                                              # Calculating arrays
from sympy import symbols, sympify                              # Calculating polynomial
import pandas as pd                                             # Printing the calculated array neatly
import matplotlib.pyplot as plt                                 # Graphing
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Saving the image of the Graph
import os                                                       # for locating file

import tkinter as tk        # For Gui
from tkinter import ttk     # Imports the table and the graph to the gui
import customtkinter as ctk # For a modern look of the gui

from CTkMessagebox import CTkMessagebox # CustomTkinter doesn't have a message box

import pygame as pg # Imports, play, and pause music

from PIL import Image, ImageTk, ImageSequence # Imports, and display Images
from time import sleep

ctk.set_appearance_mode("Dark")      # Available Modes: "Dark", "Light"
ctk.set_default_color_theme("blue")  # Available Themes: "blue", "green", "dark-blue"
plt.style.use('dark_background')     # For dark themed graph and table


def unsplash():
    splash.destroy()
    
    def music():
        global check
        if (var.get() == 1):
            pg.mixer.music.unpause()
            check = 1
            vol.set(cvol)
            vol.configure(state="normal")
        elif (var.get() == 0):
            pg.mixer.music.pause()
            check = 0
            vol.set(0)
            vol.configure(state="disabled")
            
    def poly_regression(x_data, y_data, graph_frame):
        
        eq_str = str(a2) + "*x**2 + " + str(a1) + "*x + " + str(a0)

        x, y = symbols('x y')
        eq = sympify(eq_str)
        maxed = x_data[0]
        mined = x_data[0]
        for num in x_data:
            if num > maxed:
                maxed = num
            
            if num < mined:
                mined = num
        x_line = np.linspace(mined, maxed, 20)
        y_line = np.array([eq.subs(x, xi).evalf() for xi in x_line]) + np.random.randn(len(x_line))

        x_line = x_line.astype(np.float64)
        y_line = y_line.astype(np.float64)

        poly_fit = np.polyfit(x_line, y_line, 2)
        poly_eq = np.poly1d(poly_fit)
        poly_yhat = poly_eq(x_line)
        poly_rmse = np.sqrt(np.mean((y_line - poly_yhat)**2))

        fig, ax = plt.subplots()
        ax.scatter(x_data, y_data, label='Data')
        ax.plot(x_line, poly_yhat, label=f'Polynomial Regression (RMSE={poly_rmse:.2f})')
        ax.set_title('Polynomial Regression')
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        plt.close(fig)
        canvas.get_tk_widget().bind("<Destroy>", lambda e: canvas.get_tk_widget().destroy())


    def linear_regression(x_data, y_data, graph_frame):
        lin_fit = np.polyfit(x_data, y_data, 1)
        lin_eq = np.poly1d(lin_fit)
        lin_yhat = lin_eq(x_data)
        lin_rmse = np.sqrt(np.mean((y_data - lin_yhat)**2))

        fig, ax = plt.subplots()
        ax.scatter(x_data, y_data, label='Data')
        ax.plot(x_data, lin_yhat, label=f'Linear Regression (RMSE={lin_rmse:.2f})')
        ax.set_title('Linear Regression')
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        plt.close(fig)
        canvas.get_tk_widget().bind("<Destroy>", lambda e: canvas.get_tk_widget().destroy())


    def show_graph(graph_frame, table_frame, value_frame, solve_frame):
        graph_frame.grid(row=0, column=2, padx=20, pady=(20, 10))
        table_frame.grid_forget()
        value_frame.grid_forget()
        solve_frame.grid_forget()

    def show_table(graph_frame, table_frame, value_frame, solve_frame):
        table_frame.grid(row=0, column=1, padx=20, pady=(20, 10))
        value_frame.grid(row=2, column=1, padx=20, pady=(20, 10))
        graph_frame.grid_forget()
        solve_frame.grid_forget()

    def solve(mode, frame):
        graph_frame.grid_forget()
        table_frame.grid_forget()
        value_frame.grid_forget()

        frame.grid(row=0, column=1, padx=20, pady=(20, 10))
        if mode == "Linear":
            text1 = ctk.CTkLabel(frame, text="Linear Regression \n\n\nSample Solved Linear Regression Table")
            imgl1 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(img1))
            
            text2 = ctk.CTkLabel(frame, text="\n\nSTEPS IN SOLVING LINEAR REGRESSION\n\n Step 1:\nList all given data points, xi (independent variable), and yi (dependent variable), in a table.\n Get the summation of xi as well as the yi. Then plot the values in a scatter graph.")
            imgl2 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(img2))
            imgl3 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(img3))
            
            text3 = ctk.CTkLabel(frame, text="\n\nStep 2:\nRefer to the sample solved linear regression table.\n<xiyi = multiplying each data values of xi to the data values of yi. Then get the summation of the xiyi acquired values>\n<xi^2 = get the squared data values of xi. Then get the summation of the xi^2 aquired values>\n\n\nStep 3:\nx̄ and ȳ are the means of xi and yi. To find the x̄, divide the summation of xi by the number of items (n) of the data values. Do the same for ȳ")
            imgl4 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(img4))
            
            text4 = ctk.CTkLabel(frame, text="\n\nStep 4:\nRefer to the sample solved linear regression table.\n<For (yi-ȳi)2 column, square the difference of yi and ȳi values>\n\n\nStep 5:\nGet a0 and a1 using the formula below")
            imgl5 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(img5))
            imgl6 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(img6))
            
            text5 = ctk.CTkLabel(frame, text="\n\nStep 6:\nRefer to the sample solved linear regression table.\n<For the (yi - ao - a1xi)2, square the difference of yi values, a0, and the product of a1 and xi>")
            text6 = ctk.CTkLabel(frame, text="\n\n\nQUANTIFICATION OF ERROR IN LINEAR REGRESSION\n\nStep 1:\nGet the Standard Deviation using the formula")
            imgl7 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(img7))
            
            text7 = ctk.CTkLabel(frame, text="\nNOTE: The Sr in the formula refers to the summation of (yi-ȳi)^2\n\n\nStep 2:\nGet the Standard Error of Estimate using the formula")
            imgl8 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(img8))
            
            text8 = ctk.CTkLabel(frame, text="\nNOTE: The St in the formula refers to the summation of (yi - ao - a1xi)^2\n\n\nStep 3:\nGet the Coefficient Determination using the formula")
            imgl9 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(img9))
            
            text9 = ctk.CTkLabel(frame, text="\n\nStep 4:\nGet the Correlation Coefficient using the formula")
            imgl10 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(img10))
            
            text10 = ctk.CTkLabel(frame, text="\n\nStep 5:\nFind the y where y = a0 + a1xn\n\n\n\n")

            text1.pack()
            imgl1.pack()
            text2.pack()
            imgl2.pack()
            imgl3.pack()
            text3.pack()
            imgl4.pack()
            text4.pack()
            imgl5.pack()
            imgl6.pack()
            text5.pack(), text6.pack()
            imgl7.pack()
            text7.pack()
            imgl8.pack()
            text8.pack()
            imgl9.pack()
            text9.pack()
            imgl10.pack()
            text10.pack()

        elif mode == "Poly":
            text1 = ctk.CTkLabel(frame, text="Polynomial Regression \n\n\nSample Solved Polynomial Regression Table")
            imgr1 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(rimg1))
            text2 = ctk.CTkLabel(frame, text="\n\nStep 1:\nList all the given data points of xi (independent variable) and yi (dependent variable) in a table")
            imgr2 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(rimg2))
            text3 = ctk.CTkLabel(frame, text="\n\nStep 2:\nRefer to the sample solved polynomial regression table\n<For xi^2, xi^3, and xi^4 columns, just square, cube, and raise the values to the power of four. Get the summation of the acquired values>\n<For the xiyi column, multiply the data values of xi to the data values of yi. Once acquired proceed to summation of the xiyi acquired values.>\n<For the xi2yi column, multiply the data values of xi2 to the data values of yi. Once acquired proceed to summation of the xiyi acquired values.>\n<For the (yi-ȳi)2 column, square the difference of yi and ȳi values>\n<For the (yi - ao - a1xi - a2xi2)2, square the difference of yi values, a0, the product of a1 and xi, and the product of a2 and xi2>")
            text4 = ctk.CTkLabel(frame, text="\n\nStep 3:\nRefer to the sample solved polynomial regression table\n<m is the value of the subscript of a needed. Since we only need a0, a1, and a2. The value of m is always 2 by default>\n<n refers to the number of items of xi and yi values>\n<The mean or x̄i is acquired by dividing the summation of values of xi by the number of items. Do the same with yi.>\n\n\nStep 5:\n")
            imgr3 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(rimg3))
            text5 = ctk.CTkLabel(frame, text="<Solve this using Gaussian Elimination or use Caltech: Mode-5-2>\n<You can now have the values of a0, a1, and a2. The least-squares quadratic equation for this is y = a0 + a1x + a2x2>")
            text6 = ctk.CTkLabel(frame, text="\n\nQUANTIFICATION OF POLYNOMIAL REGRESSION\n\nStep 1:\nGet the Standard Error of Estimate using the formula")
            imgr4 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(rimg4))
            text7 = ctk.CTkLabel(frame, text="\nNOTE: The Sr in the formula refers to the summation of (yi - ao - a1xi - a2xi2)2.\n\nStep 3: Get the Coefficient Determination using the formula")
            imgr5 = ctk.CTkLabel(frame, image=ImageTk.PhotoImage(img9))
            text8 = ctk.CTkLabel(frame, text="\nNOTE: The St in the formula is the summation of (yi-ȳi)2 .\n\nStep 4:\nGet the Correlation Coefficient using the formula by getting the square root of Coefficient Determination.\n\n\n\n")

            text1.pack(), imgr1.pack(), text2.pack(), imgr2.pack(), text3.pack(), text4.pack(), imgr3.pack(), text5.pack(), text6.pack(), imgr4.pack(), text7.pack(), imgr5.pack(), text8.pack()         

    def calculate_poly(number_items): 
        global table_b, graph_b, value_frame, graph_frame, table_frame, solve_frame, placeholder, backs3, solut_b, title, a0, a1, a2, title_frame
        try:
            differences = [y_values[i+1] - y_values[i] for i in range(len(y_values)-1)]
            checker = all(diff == differences[0] for diff in differences)

            if checker == True:
               raise ValueError 
            xi = np.array(x_values)
            yi = np.array(y_values)
            xi2 = xi ** 2
            xi3 = xi ** 3
            xi4 = xi ** 4
            xiyi = xi * yi
            xi2yi = xi2 * yi
            backs2.place_forget()
            #computations of poly
            tframe.place_forget()

            # Setting up matrix
            n = 3 
            a = np.zeros((n,n+1))

            a[0][0] = number_items
            a[0][1] = xi.sum()
            a[0][2] = xi2.sum()
            a[0][3] = yi.sum()
            a[1][0] = xi.sum()
            a[1][1] = xi2.sum()
            a[1][2] = xi3.sum()
            a[1][3] = xiyi.sum()
            a[2][0] = xi2.sum()
            a[2][1] = xi3.sum()
            a[2][2] = xi4.sum()
            a[2][3] = xi2yi.sum()

            x = np.linalg.solve(a[:,:n], a[:,n])
            a0, a1, a2 = x[0], x[1], x[2]

            a0 = a0.round(4)
            a1 = a1.round(4)
            a2 = a2.round(4)

            data = {"Xi": xi, "Yi": yi, "(Xi)^2": xi2, "(Xi)^3": xi3, "(Xi)^4": xi4, "Xi*Yi": xiyi, "Xi^2*Yi": xi2yi}
            df = pd.DataFrame(data, index=range(1, number_items+1))

            x_bar = df['Xi'].sum() / number_items
            y_bar = df['Yi'].sum() / number_items
            yi_y2 = df['Yi']-y_bar
            yi_ybar2Final = yi_y2**2

            df['(Yi-Ȳ)^2'] = yi_ybar2Final

            last = ((yi - a0) - (a1 * xi) - (a2 * xi2))**2
            df['(Yi - a0 - a1*Xi - a2*Xi2)^2'] = last
            
            

            S = (last.sum() / (number_items - 3))**(0.5)
            r = ((df['(Yi-Ȳ)^2'].sum() - last.sum()) / df['(Yi-Ȳ)^2'].sum())

            df.loc['Σ'] = df.sum()
            df = df.round(4)
            
            graph_frame = ctk.CTkFrame(root)
            table_frame = ctk.CTkFrame(root)
            value_frame = ctk.CTkTextbox(root, width=250)
            solve_frame = ctk.CTkScrollableFrame(root, width=900, height=400)
            text =  "m   = 2" + "\n\nn   = " + str(number_items) + "\n\nX̄   = " + str(x_bar) + "\n\nȲ   = " + "\n\na0 = " + str(a2) + "x^2\n\na1 = " + str(a1) + "x\n\na2 = " + str(a0) + "" + "\n\nX̄   = " + str(x_bar) + "\n\nȲ   = " + str(y_bar) + "\n\nS   = " + str(S) + "\n\nr2 = " + str(r)
            value_frame.insert("0.0", text)
            title_frame = ctk.CTkFrame(root, width=225, height=500, fg_color="transparent")
            title_frame.place(relx=0.075, rely=0.5, anchor="center")


            placeholder = ctk.CTkLabel(root, text="                         ", font=ctk.CTkFont(size=20, weight="bold"))
            placeholder.grid(row=0, column=0, padx=20, pady=(20, 10))
            title = ctk.CTkLabel(root, text="Polynomial", font=ctk.CTkFont(size=20, weight="bold"))
            title.place(x=10, y=40)
            graph_b = ctk.CTkButton(root, text="Show Graph", command=lambda: show_graph(graph_frame, table_frame, value_frame, solve_frame))
            graph_b.place(x=10, y=80)
            table_b = ctk.CTkButton(root, text="Show Table", command=lambda: show_table(graph_frame, table_frame, value_frame, solve_frame))
            table_b.place(x=10, y=120)
            solut_b = ctk.CTkButton(root, text="How to solve", command=lambda: solve("Poly", solve_frame))
            solut_b.place(x=10, y=160)

            poly_regression(xi, yi, graph_frame)

            style.layout("Custom.Treeview",
                        [('Custom.Treeview.treearea', {'sticky': 'nswe'})])
            style.configure("Custom.Treeview",
                        background="#444444",
                        foreground="white",
                        fieldbackground="#444444",
                        font=("Arial", 12))
            tree = ttk.Treeview(table_frame, style="Custom.Treeview", show="headings")

            tree["columns"] = ["Index"] + list(df.columns)
            tree.column("Index", width=50)
            tree.heading("Index", text=df.index.name or "Index")


            for col in tree["columns"][1:]:
                tree.column(col, width=125)
                tree.heading(col, text=col)


            for i, row in df.iterrows():
                values = [i] + list(row.values)
                tree.insert("", "end", text=i, values=values)

            tree.pack(fill=tk.BOTH, expand=True)

            graph_frame.grid(row=0, column=1, padx=20, pady=(20, 10))
            backs3 = ctk.CTkButton(root, text="BACK", command=lambda: back(3, 0), width=150, height=30)
            backs3.place(relx=0.075, rely=0.95, anchor="center")
        except ValueError:
            back("errored", "Poly")


    def calculate_linear(number_items):
        global table_b, graph_b, value_frame, graph_frame, table_frame, solve_frame, placeholder, solut_b, backs3, title, title_frame
        
        backs2.place_forget()
        #computations of linear
        tframe.place_forget()
        xi = np.array(x_values)
        yi = np.array(y_values)
        xiyi = xi * yi
        xi2 = xi ** 2

        data = {"Xi": xi, "Yi": yi, "Xi*Yi": xiyi, "(Xi)^2": xi2}
        df = pd.DataFrame(data, index=range(1, number_items+1))

        x_bar = df['Xi'].sum() / number_items
        y_bar = df['Yi'].sum() / number_items
        yi_y2 = df['Yi']-y_bar
        yi_ybar2Final = yi_y2**2

        df['(Yi-Ȳ)^2'] = yi_ybar2Final

        a1 = (((number_items * df['Xi*Yi'].sum()) - (df['Xi'].sum() * df['Yi'].sum())) / ((number_items * df['(Xi)^2'].sum()) - (df['Xi'].sum()**2)))
        a0 = (y_bar - (a1 * x_bar))
        last = ((yi - a0 - (a1 * xi))**2)

        df['(Yi - a0 - a1*Xi)^2'] = last
        
        
        
        Sy = (df['(Yi-Ȳ)^2'].sum() / (number_items - 1))**(1/2)
        S = (df['(Yi - a0 - a1*Xi)^2'].sum() / (number_items -2))**(1/2)

        r2 = ((df['(Yi-Ȳ)^2'].sum() - df['(Yi - a0 - a1*Xi)^2'].sum()) / df['(Yi-Ȳ)^2'].sum())

        r = r2**(0.5)

        df.loc['Σ'] = df.sum()

        df = df.round(4)

        graph_frame = ctk.CTkFrame(root)
        table_frame = ctk.CTkFrame(root)
        value_frame = ctk.CTkTextbox(root, width=250)
        solve_frame = ctk.CTkScrollableFrame(root, width=900, height=400)
        text =  "a1 = " + str(a1) + "\n\na0 = " + str(a0) + "x\n\nX̄   = " + str(x_bar) + "\n\nȲ   = " + str(y_bar) + "\n\nSy = " + str(Sy) + "\n\nSy/s= " + str(S) + "\n\nr2 = " + str(r2) + "\n\nr   = " + str(r)
        value_frame.insert("0.0", text)
        title_frame = ctk.CTkFrame(root, width=225, height=500, fg_color="transparent")
        title_frame.place(relx=0.075, rely=0.5, anchor="center")

        placeholder = ctk.CTkLabel(root, text="                         ", font=ctk.CTkFont(size=20, weight="bold"))
        placeholder.grid(row=0, column=0, padx=20, pady=(20, 10))
        title = ctk.CTkLabel(root, text="Linear", font=ctk.CTkFont(size=20, weight="bold"))
        title.place(x=10, y=40)
        graph_b = ctk.CTkButton(root, text="Show Graph", command=lambda: show_graph(graph_frame, table_frame, value_frame, solve_frame))
        graph_b.place(x=10, y=80)
        table_b = ctk.CTkButton(root, text="Show Table", command=lambda: show_table(graph_frame, table_frame, value_frame, solve_frame))
        table_b.place(x=10, y=120)
        solut_b = ctk.CTkButton(root, text="How to solve", command=lambda: solve("Linear", solve_frame))
        solut_b.place(x=10, y=160)

        linear_regression(xi, yi, graph_frame)

        style.layout("Custom.Treeview",
                    [('Custom.Treeview.treearea', {'sticky': 'nswe'})])
        style.configure("Custom.Treeview",
                    background="#444444",
                    foreground="white",
                    fieldbackground="#444444",
                    font=("Arial", 12))
        tree = ttk.Treeview(table_frame, style="Custom.Treeview", show="headings")

        tree["columns"] = ["Index"] + list(df.columns)
        tree.column("Index", width=100)
        tree.heading("Index", text=df.index.name or "Index")


        for col in tree["columns"][1:]:
            tree.column(col, width=180)
            tree.heading(col, text=col)


        for i, row in df.iterrows():
            values = [i] + list(row.values)
            tree.insert("", "end", text=i, values=values)

        tree.pack(fill=tk.BOTH, expand=True)

        graph_frame.grid(row=0, column=1, padx=20, pady=(20, 10))
        backs3 = ctk.CTkButton(root, text="BACK", command=lambda: back(3, 0), width=150, height=30)
        backs3.place(relx=0.075, rely=0.95, anchor="center")


    def add_value(value_list, frame, entry_widget, max_count, calc_button):
        
        try:
            value = float(entry_widget.get())
            value_list.append(value)
            label = ctk.CTkLabel(frame, text=entry_widget.get())
            label.pack()
            entry_widget.delete(0, tk.END)
            
            
            # disable input and button if max count is reached
            if len(x_values) == max_count:
                entry_x.unbind('<Return>')
                entry_x.configure(state="disabled")
                button_x.configure(state="disabled")
                if entry_y.cget('state') != "disabled":
                    entry_y.focus_set()
            
            if len(y_values) == max_count:
                entry_y.unbind('<Return>')
                entry_y.configure(state="disabled")
                button_y.configure(state="disabled")
                if entry_x.cget('state') != "disabled":
                    entry_x.focus_set()
            
            if entry_x.cget('state') == entry_y.cget('state') == "disabled":
                calc_button.configure(state="normal")
                return
                
        except ValueError:
            CTkMessagebox(title="Error", message="Invalid Input", icon="cancel")
            entry_widget.delete(0, 'end')
        

    
    def validate_entry(text):
        if text in '0123456789':
            return True
        elif text == "Enter here":
            return True
        elif text == "":
            return True
        else:
            return False
            
    def next_step(mode):
        global entry_x, entry_y, button_x, button_y, tframe, backs2, x_values, y_values
        x_values = [] # Set Values
        y_values = [] #
        try:
            max_count = int(number_itemsentry.get())
            if mode == "Linear":
                if max_count < 2:
                    raise ValueError
            elif mode == "Poly":
                if max_count < 3:
                    raise ValueError
            
            background(fps5)
            backs.place_forget()
            
            startf.place_forget()
            tframe = ctk.CTkFrame(root)
            tframe.place(relx=0.5, rely=0.5, anchor="center")
            x_frame = ctk.CTkFrame(tframe)
            x_frame.pack(side="left")
            y_frame = ctk.CTkFrame(tframe)
            y_frame.pack(side="left")

            x_f = ctk.CTkScrollableFrame(x_frame)
            labx = ctk.CTkLabel(x_f, text="Xi list")
            entry_x_label = ctk.CTkLabel(x_frame, text="Add X Value:")
            entry_x_label.pack()
            entry_x = ctk.CTkEntry(x_frame, width=150, height=30, placeholder_text="Enter xi here...")
            entry_x.bind('<Return>', lambda event: add_value(x_values, x_f, entry_x, max_count, calc_button))
            entry_x.pack(padx=5, pady=2)
            button_x = ctk.CTkButton(x_frame, text="Add X", command=lambda: add_value(x_values, x_f, entry_x, max_count, calc_button), width=150, height=30)
            button_x.pack(padx=5, pady=2), x_f.pack(), labx.pack()
            entry_x.focus_set()
            # create y input widgets
            y_f = ctk.CTkScrollableFrame(y_frame)
            laby = ctk.CTkLabel(y_f, text="Yi list")
            entry_y_label = ctk.CTkLabel(y_frame, text="Add Y Value:")
            entry_y_label.pack()
            entry_y = ctk.CTkEntry(y_frame, width=150, height=30, placeholder_text="Enter yi here...")
            entry_y.bind('<Return>', lambda event: add_value(y_values, y_f, entry_y, max_count, calc_button))
            entry_y.pack(padx=5, pady=2)
            button_y = ctk.CTkButton(y_frame, text="Add Y", command=lambda: add_value(y_values, y_f, entry_y, max_count, calc_button), width=150, height=30)
            button_y.pack(padx=5, pady=2), y_f.pack(), laby.pack()
            
            if mode == "Linear":
                calc_button = ctk.CTkButton(tframe, text="Calculate", state="disabled", command=lambda: calculate_linear(max_count), width=150, height=30)
                
            elif mode == "Poly":
                calc_button = ctk.CTkButton(tframe, text="Calculate", state="disabled", command=lambda: calculate_poly(max_count), width=150, height=30)
            calc_button.pack(side="left")

            backs2 = ctk.CTkButton(root, text="BACK", command=lambda: back(2, mode), width=150, height=30)
            backs2.place(relx=0.075, rely=0.95, anchor="center")
            root.bind('<Escape>', lambda event: back(2, mode)) 
        except ValueError:
            if mode == "Linear":
                CTkMessagebox(title="Error", message="Invalid Input\nMust be 2 or higher", icon="cancel")
            elif mode == "Poly":
                CTkMessagebox(title="Error", message="Invalid Input\nMust be 3 or higher", icon="cancel")
            
            number_itemsentry.delete(0, 'end')

    def start(mode):
        global startf, number_itemsentry, backs
    
        if mode == "Linear":
            background(fps2)
        elif mode == "Poly":
            background(fps3)
        main.place_forget()
        startf = ctk.CTkFrame(root)
        
        direct = ctk.CTkLabel(startf, text="How many items are in the table?")
        number_itemsentry = ctk.CTkEntry(startf, width=150, height=30, validate="key", validatecommand=(root.register(validate_entry), "%S"), placeholder_text="Enter here")
        number_itemsentry.bind('<Return>', lambda event: next_step(mode))

        next_stepbtn = ctk.CTkButton(startf, text="Continue", command=lambda: next_step(mode), width=150, height=30)
        startf.place(relx=0.5, rely=0.25, anchor="center"), direct.pack(padx=5, pady=2), number_itemsentry.pack(padx=5, pady=2), next_stepbtn.pack(padx=5, pady=2)

        backs = ctk.CTkButton(root, text="BACK", command=lambda: back(1, mode), width=150, height=30)
        backs.place(relx=0.075, rely=0.95, anchor="center")
        root.bind('<Escape>', lambda event: back(1, mode))
        root.protocol("WN_DELETE_WINDOW", EXITWIN)

    def back(mode, save):
        if mode == 1:
            startf.place_forget()
            backs.place_forget()
            mainm()
        elif mode == 2:
            msg = CTkMessagebox(title="Exit?", message="You might have some unsaved changes on this tab", icon="warning", option_1="Stay", option_2="Leave", button_hover_color="grey50")
            response = msg.get()
            
            if response=="Leave":
                
                backs2.place_forget()
                tframe.place_forget()
                start(save)
        elif mode == "errored":
            msg = CTkMessagebox(title="Exit?", message="Your Yi must not have the same difference\nIt only works on Linear", icon="warning", option_1="Go Back", button_hover_color="grey50")
            response = msg.get()
            
            if response=="Go Back":
                backs2.place_forget()
                tframe.destroy()
                next_step(save)
        
        elif mode == 3:

            msg = CTkMessagebox(message="Thank you <3",icon="check", option_1="Stay", option_2="Main menu")
            response = msg.get()

            if response=="Main menu":
                table_frame.grid_forget()
                graph_frame.grid_forget()
                placeholder.grid_forget()
                value_frame.grid_forget()
                solve_frame.grid_forget()
                table_b.place_forget()
                graph_b.place_forget()
                solut_b.place_forget()
                title_frame.place_forget()
                title.place_forget()
                backs3.place_forget()
                
                mainm()

    def aboutTab():
        global descript_frame, backset
        background(fps5)
        set.place_forget()
        descript_frame = ctk.CTkScrollableFrame(root, width=1000, height=400)
        backset = ctk.CTkButton(root, text="BACK", command=lambda: settings(2), width=150, height=30)
        text1 = ctk.CTkLabel(descript_frame, text="Meet The Team\n\nASTURIAS, JOHN MICKUS A.\nCEREZO, ARIANE M.\nFETALSANA, CIARA THAMAR R.\nGARCIA, JARELL D.\nMANALO, JAYSON J.\nPASOOT, MARCO YVAN T.\nPRANADA, JOHN KENNETH P.\nRIBAYA, JOHN NICOLAI C.\n\n\n\nAbout The App:\n\nThrough this project,\nit made it easier for students to understand least square regression by creating a user-friendly calculator program.\nThe program allows users to estimate the parameters of a linear equation that best fits a given dataset by using this method.\n\nOur aim with this project was to make the process of least squares regression simpler, especially for students who are new to the topic. \nUsers can comprehend the underlying concepts and calculations involved in this statistical technique more easily with our program's step-by-step guidance and explanations.\n\nOverall, our project aims to help students enhance their analytical skills and utilize them to solve real-life issues,\nultimately leading to success in both academic and professional endeavors.\n\n\n\nLeast Square Regression (linear and polynomial)\nis one of the lessons in Numerical Methods that requires patience and attention to detail in acquiring specific data especially when manual computations are used.\nIn this topic, tables and graphs represent the answer. However, it requires repeated iterations, statistical concepts, and various techniques\nto obtain an optimal solution which usually takes so much time to do.\nUsing manual calculations, there is also a tendency of having errors in the rounding process, the accuracy of answers, and acquiring final solutions.\n\nThis project aims to address the struggles of students in solving least square regression and provide students with a highly accurate, consistent, efficient, and reusable tool.\nThis will help the students to understand the lesson easier since this project provides a visual representation of results.\nMoreover, this project can also help students enhance their critical thinking and\nproblem-solving skills which could help them apply their learnings in actual activities regarding least square regression. ")
        descript_frame.place(relx=0.5, rely=0.475, anchor="center"), backset.place(relx=0.5, rely=0.95, anchor="center"), text1.pack()
            
    def volume(value):
        global cvol
        cvol = vol.get()
        pg.mixer.music.set_volume(vol.get())

    def settings(modeint):
        global var, set, vol
        background(fps4)
        if modeint == 1:
            main.place_forget()
        elif modeint == 2:
            descript_frame.place_forget()
            backset.place_forget()
        var = tk.IntVar()
        set = ctk.CTkFrame(root)
        musical = ctk.CTkCheckBox(set, text="MUSIC", command=lambda: music(), variable=var) 
        vol = ctk.CTkSlider(set, from_=0, to=1, command= volume)
        vol.set(cvol)
        
        

        if check == 1:
            musical.select()
            vol.set(cvol)
            vol.configure(state="normal")
        elif check == 0:
            musical.deselect()
            vol.set(0)
            vol.configure(state="disabled")
        back = ctk.CTkButton(set, text="Done", command=lambda: done(), width=150, height=30)
        about = ctk.CTkButton(set, text="About", command=lambda: aboutTab(), width=150, height=30)
        set.place(relx=0.5, rely=0.25, anchor="center"), musical.pack(padx=5, pady=2), vol.pack(padx=5, pady=2), about.pack(padx=5, pady=2), back.pack(padx=5, pady=2)
        

    def done():
        set.place_forget()
        mainm()

    def mainm():
        global main
        
        background(fps1)
        main = ctk.CTkFrame(root)
        main.place(relx=0.5, rely=0.25, anchor="center")
        

        linear = ctk.CTkButton(main, text="Linear Regression", command=lambda: start("Linear"), width=150, height=30)
        poly = ctk.CTkButton(main, text="Polynomial Regression", command=lambda: start("Poly"), width=150, height=33)
        set = ctk.CTkButton(main, text="Settings", command=lambda: settings(1), width=150, height=30)
        linear.pack(padx=5, pady=2), poly.pack(padx=5, pady=2), set.pack(padx=5, pady=2)
    
    def play_bg(repeat, fps, fps_counter):
        bg.configure(image=fps[fps_counter])
        fps_counter += 1
        if fps_counter == len(fps):
            fps_counter = 0
            
        if repeat == 40:
            pass
            
        elif rep >= 0 and rep < 40:  
            repeat = repeat + 1
            root.after(20, play_bg, repeat, fps, fps_counter)

    def background(fps):
        
        
        repeat = 0

        play_bg(repeat, fps, 1)
        
            


    def EXITWIN():
        root.quit()

    pg.mixer.init()          
    pg.mixer.music.load(os.path.join(dir_path,"DATA\Inhale.wav"))  
    

    root = ctk.CTk()
    root.resizable(False, False)

    style = ttk.Style()
    root.title("Regression")
    
    window_width = 1175
    window_height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
    
    bg = ctk.CTkLabel(root, text="", width=1175, height=500)
    bg.place(relx=0.5, rely=0.5, anchor="center")

    root.protocol("WN_DELETE_WINDOW", EXITWIN)

    #Adding extra files
    img1 = Image.open(os.path.join(dir_path,"DATA\L1.png"))
    img2 = Image.open(os.path.join(dir_path,"DATA\L2.png"))
    img3 = Image.open(os.path.join(dir_path,"DATA\L3.png"))
    img4 = Image.open(os.path.join(dir_path,"DATA\L4.png"))
    img5 = Image.open(os.path.join(dir_path,"DATA\L5.png"))
    img6 = Image.open(os.path.join(dir_path,"DATA\L6.png"))
    img7 = Image.open(os.path.join(dir_path,"DATA\L7.png"))
    img8 = Image.open(os.path.join(dir_path,"DATA\L8.png"))
    img9 = Image.open(os.path.join(dir_path,"DATA\L9.png"))
    img10 = Image.open(os.path.join(dir_path,"DATA\L10.png"))
    rimg1 = Image.open(os.path.join(dir_path,"DATA\P1.png"))
    rimg2 = Image.open(os.path.join(dir_path,"DATA\P2.png"))
    rimg3 = Image.open(os.path.join(dir_path,"DATA\P3.png"))
    rimg4 = Image.open(os.path.join(dir_path,"DATA\P4.png"))
    gif1 = Image.open(os.path.join(dir_path,"DATA\GUI final project (1).gif"))
    gif2 = Image.open(os.path.join(dir_path,"DATA\GUI final project (2).gif"))
    gif3 = Image.open(os.path.join(dir_path,"DATA\GUI final project (3).gif"))
    gif4 = Image.open(os.path.join(dir_path,"DATA\GUI final project (4).gif"))
    gif5 = Image.open(os.path.join(dir_path,"DATA\GUI final project(5).gif"))

    fps1 = []
    for frames in ImageSequence.Iterator(gif1):
        fps1.append(ImageTk.PhotoImage(frames))
    fps2 = []
    for frames in ImageSequence.Iterator(gif2):
        fps2.append(ImageTk.PhotoImage(frames))
    fps3 = []
    for frames in ImageSequence.Iterator(gif3):
        fps3.append(ImageTk.PhotoImage(frames))
    fps4 = []
    for frames in ImageSequence.Iterator(gif4):
        fps4.append(ImageTk.PhotoImage(frames))
    fps5 = []
    for frames in ImageSequence.Iterator(gif5):
        fps5.append(ImageTk.PhotoImage(frames))
    pg.mixer.music.play(loops=-1)
    # Calling main menu
    mainm()

    root.mainloop()


#Splash screen
def play_gif0(frame_idx, rep, frames, mode):
    label.config(image=frames[frame_idx])
    frame_idx += 1
    if frame_idx == len(frames):
        frame_idx = 0
        
    if rep == 90:
        if mode == 1:
            unsplash()
        elif mode == 0:
            rep = 0
            play_gif0(0, rep, frames2, 1)
    elif rep >= 50 and rep < 90:
        rep = rep + 1
        splash.after(55, play_gif0, frame_idx, rep, frames, mode)
        
    elif rep >= 0 and rep < 50:  
        rep = rep + 1
        splash.after(25, play_gif0, frame_idx, rep, frames, mode)   


check = 1
cvol = 0.25
dir_path = os.path.dirname(os.path.realpath(__file__))

splash = tk.Tk()
splash.overrideredirect(True)
window_width = 500
window_height = 500

screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

splash.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
rep = 0

gif0 = Image.open(os.path.join(dir_path,"DATA\groupFury.gif"))
gif01 = Image.open(os.path.join(dir_path,"DATA\MegaFury.gif"))

frames1 = []
for frame in ImageSequence.Iterator(gif0):
    frames1.append(ImageTk.PhotoImage(frame))
frames2 = []
for frame in ImageSequence.Iterator(gif01):
    frames2.append(ImageTk.PhotoImage(frame))


label = tk.Label(splash)
label.pack()



play_gif0(0, rep, frames1, 0)


splash.mainloop()