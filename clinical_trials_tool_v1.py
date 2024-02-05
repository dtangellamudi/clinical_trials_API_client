#Import Libraries

import json
import tkinter as tk
from tkinter import ttk, Scrollbar
from tkinter import messagebox
from pytrials.client import ClinicalTrials

######################################################

def submit():
    search = search_entry.get()
    count = int(count_entry.get())

    if search == "" or count == "":
        messagebox.showerror("Error", "Please enter both search phrase and number of studies required.")
    else:
        ct = ClinicalTrials()
        full_studies = ct.get_full_studies(search_expr = search, max_studies = int(count))
        create_studies_window(full_studies)  


def create_studies_window(full_studies):
    root = tk.Tk()
    root.title('List of Studies')
    root.geometry('1278x720')
    root.configure(bg='DodgerBlue4')

    # Create a frame to contain both the LabelFrame and Treeview
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")  # Make the frame expand to fill the window

    # Center the frame in the window
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)


    input_frame = tk.LabelFrame(frame, font=('Consolas',14))
    input_frame.grid(row=0,column=0,rowspan=8,columnspan=4)

    l1 = tk.Label(input_frame,  anchor="w", width=24, height=1, relief="ridge", text="Rank", font=('Consolas',14)).grid(row=1, column=0)

    l2 = tk.Label(input_frame,  anchor="w", width=24, height=1, relief="ridge", text="NCTid", font=('Consolas',14)).grid(row=2, column=0)

    l3 = tk.Label(input_frame,  anchor="w", width=24, height=1, relief="ridge", text="Organization Study ID", font=('Consolas',14)).grid(row=3, column=0)

    l4 = tk.Label(input_frame,  anchor="w", width=24, height=1, relief="ridge", text="Organization Name", font=('Consolas',14)).grid(row=4, column=0)

    l5 = tk.Label(input_frame,  anchor="w", width=24, height=1, relief="ridge", text="Organization Class", font=('Consolas',14)).grid(row=5, column=0)

    l6 = tk.Label(input_frame,  anchor="w", width=24, height=1, relief="ridge", text="Brief Study Title", font=('Consolas',14)).grid(row=6, column=0)

    l7 = tk.Label(input_frame,  anchor="w", width=24, height=1, relief="ridge", text="Full Study Title", font=('Consolas',14)).grid(row=7, column=0)

    l8 = tk.Label(input_frame,  anchor="w", width=24, height=1, relief="ridge", text="Acronym", font=('Consolas',14)).grid(row=8, column=0)

    crm_rank = tk.Entry(input_frame,width=100,borderwidth=2,fg="black",font=('Consolas',14))
    crm_rank.grid(row=1, column=1,columnspan=2)

    crm_nctid = tk.Entry(input_frame,width=100,borderwidth=2,fg="black",font=('Consolas',14))
    crm_nctid.grid(row=2, column=1,columnspan=2)

    crm_orgid = tk.Entry(input_frame,width=100,borderwidth=2,fg="black",font=('Consolas',14))
    crm_orgid.grid(row=3, column=1,columnspan=2)

    crm_orgname = tk.Entry(input_frame,width=100,borderwidth=2,fg="black",font=('Consolas',14))
    crm_orgname.grid(row=4, column=1,columnspan=2)

    crm_orgclass = tk.Entry(input_frame,width=100,borderwidth=2,fg="black",font=('Consolas',14))
    crm_orgclass.grid(row=5, column=1,columnspan=2)

    crm_brftitle = tk.Entry(input_frame,width=100,borderwidth=2,fg="black",font=('Consolas',14))
    crm_brftitle.grid(row=6, column=1,columnspan=2)

    crm_fulltitle = tk.Entry(input_frame,width=100,borderwidth=2,fg="black",font=('Consolas',14))
    crm_fulltitle.grid(row=7, column=1,columnspan=2)

    crm_acro = tk.Entry(input_frame,width=100,borderwidth=2,fg="black",font=('Consolas',14))
    crm_acro.grid(row=8, column=1,columnspan=2)

#######################################################################################################################################################################

    trv =ttk.Treeview(frame, columns=(1,2,3,4,5,6,7,8),show="headings",height="16")
    trv.grid(row=11,column=0, rowspan=16,columnspan=8)

    trv.heading(1,text="Rank", anchor="center")
    trv.heading(2,text="NCTid", anchor="center")
    trv.heading(3,text="Organization Study ID", anchor="center")
    trv.heading(4,text="Organization Name", anchor="center")
    trv.heading(5,text="Organization Class", anchor="center")
    trv.heading(6,text="Brief Title", anchor="center")
    trv.heading(7,text="Full Title", anchor="center")
    trv.heading(8,text="Acronym", anchor="center")


    trv.column("#1",anchor="w",width=50, stretch=True)
    trv.column("#2",anchor="w", width=140, stretch=True)
    trv.column("#3",anchor="w", width=140, stretch=True)
    trv.column("#4",anchor="w", width=240, stretch=True)
    trv.column("#5",anchor="w", width=100, stretch=True)
    trv.column("#6",anchor="w", width=240, stretch=True)
    trv.column("#7",anchor="w", width=240, stretch=True)
    trv.column("#8",anchor="w", width=140, stretch=True)

    # Create a vertical scrollbar
    scrollbar = Scrollbar(root, orient="vertical", command=trv.yview)
    scrollbar.grid(row=11, column=8, rowspan=16, sticky='ns')

    # Configure Treeview to use the scrollbar
    trv.configure(yscrollcommand=scrollbar.set)

    my_study_list = full_studies['FullStudiesResponse']['FullStudies']

    def load_trv_with_json():

        rowIndex=1

        for study in my_study_list:

            rank = study['Rank']
            NCTid = study['Study']['ProtocolSection']['IdentificationModule']['NCTId']
            Org_Study_ID = study['Study']['ProtocolSection']['IdentificationModule']['OrgStudyIdInfo']['OrgStudyId']
            Org_Name = study['Study']['ProtocolSection']['IdentificationModule']['Organization']['OrgFullName']
            Org_Class = study['Study']['ProtocolSection']['IdentificationModule']['Organization']['OrgClass']
            Brf_Title = study['Study']['ProtocolSection']['IdentificationModule']['BriefTitle']
            Full_Title = study['Study']['ProtocolSection']['IdentificationModule']['OfficialTitle']
            Acronym = study['Study']['ProtocolSection']['IdentificationModule'].get('Acronym', 'N/A')

            
            trv.insert('',index='end',iid=rowIndex,text="",
                values=(rank, NCTid, Org_Study_ID, Org_Name, Org_Class, Brf_Title, Full_Title, Acronym))
            rowIndex=rowIndex+1



    def load_edit_field_with_row_data(_tuple):
        if len(_tuple)==0:
            return;

        crm_rank.delete(0,tk.END)
        crm_rank.insert(0,_tuple[0])
        crm_nctid.delete(0,tk.END)
        crm_nctid.insert(0,_tuple[1])
        crm_orgid.delete(0,tk.END)
        crm_orgid.insert(0,_tuple[2])
        crm_orgname.delete(0,tk.END)
        crm_orgname.insert(0,_tuple[3])
        crm_orgclass.delete(0,tk.END)
        crm_orgclass.insert(0,_tuple[4])
        crm_brftitle.delete(0,tk.END)
        crm_brftitle.insert(0,_tuple[5])
        crm_fulltitle.delete(0,tk.END)
        crm_fulltitle.insert(0,_tuple[6])
        crm_acro.delete(0,tk.END)
        crm_acro.insert(0,_tuple[7])

    def MouseButtonUpCallBack(event):
        currentRowIndex = trv.selection()[0]
        lastTuple = (trv.item(currentRowIndex,'values'))
        load_edit_field_with_row_data(lastTuple)


    def open_new_window(data, study_index):
        new_window = tk.Toplevel(root)
        new_window.title(f"{full_studies['FullStudiesResponse']['FullStudies'][study_index]['Study']['ProtocolSection']['IdentificationModule']['BriefTitle']}")

   #######################################################
        def create_status_window():
            status_window = tk.Toplevel(new_window)
            status_window.title("Status")

            i=0

            statusmodule = full_studies['FullStudiesResponse']['FullStudies'][study_index]['Study']['ProtocolSection']['StatusModule']

            for key in statusmodule:
                key_value = statusmodule[key]
                if type(key_value) == dict:
                    for key2 in key_value:
                        key2_value = key_value[key2]
                        label = tk.Label(status_window, text= key2, width=40, anchor='w')
                        label.grid(row=i, column=0, padx=5, pady=5)
                        value = tk .Label(status_window, text=key2_value, width=80, anchor='w')
                        value.grid(row=i, column=1, padx=5, pady=5)
                        i+=1
                else: 
                    label = tk.Label(status_window, text= key, width=40, anchor='w')
                    label.grid(row=i, column=0, padx=5, pady=5)
                    value = tk.Label(status_window, text=key_value, width=80, anchor='w')
                    value.grid(row=i, column=1, padx=5, pady=5)
                    i+=1
    
    #################################################################################
        
        def create_sponsor_window():
            sponsor_window = tk.Toplevel(new_window)
            sponsor_window.title("Sponsors/Collaborators")

            i=0

            sponsormodule = full_studies['FullStudiesResponse']['FullStudies'][study_index]['Study']['ProtocolSection']['SponsorCollaboratorsModule']

            for key in sponsormodule:
                key_value = sponsormodule[key]
                if type(key_value) == dict:
                    for key2 in key_value:
                        key2_value = key_value[key2]
                        label = tk.Label(sponsor_window, text= key2, width=40, anchor='w')
                        label.grid(row=i, column=0, padx=5, pady=5)
                        value = tk.Label(sponsor_window, text=key2_value, width=80, anchor='w')
                        value.grid(row=i, column=1, padx=5, pady=5)
                        i+=1
                else: 
                    label = tk.Label(sponsor_window, text= key, width=40, anchor='w')
                    label.grid(row=i, column=0, padx=5, pady=5)
                    value = tk.Label(sponsor_window, text=key_value, width=80, anchor='w')
                    value.grid(row=i, column=1, padx=5, pady=5)
                    i+=1
        
        
    #################################################################################

        def create_oversight_window():
            oversight_window = tk.Toplevel(new_window)
            oversight_window.title("Oversight")

            i=0

            oversightmodule = full_studies['FullStudiesResponse']['FullStudies'][study_index]['Study']['ProtocolSection']['OversightModule']

            for key in oversightmodule:
                key_value = oversightmodule[key]
                if type(key_value) == dict:
                    
                    for key2 in key_value:
                        key2_value = key_value[key2]
                        label = tk.Label(oversight_window, text= key2, width=40, anchor='w')
                        label.grid(row=i, column=0, padx=5, pady=5)
                        value = tk.Label(oversight_window, text=key2_value, width=80, anchor='w')
                        value.grid(row=i, column=1, padx=5, pady=5)
                        i+=1
                else: 
                    label = tk.Label(oversight_window, text= key, width=40, anchor='w')
                    label.grid(row=i, column=0, padx=5, pady=5)
                    value = tk.Label(oversight_window, text=key_value, width=80, anchor='w')
                    value.grid(row=i, column=1, padx=5, pady=5)
                    i+=1
        
        
    ################################################################################# 
       
        def create_description_window():
            description_window = tk.Toplevel(new_window)
            description_window.title("Description")

            i=0

            descriptionmodule = full_studies['FullStudiesResponse']['FullStudies'][study_index]['Study']['ProtocolSection']['DescriptionModule']

            for key in descriptionmodule:
                key_value = descriptionmodule[key]
                if type(key_value) == dict:

                    for key2 in key_value:
                        key2_value = key_value[key2]
                        label = tk.Label(description_window, text= key2, width=40, anchor='w')
                        label.grid(row=i, column=0, padx=5, pady=5, sticky='nw')
                        value = tk.Label(description_window, text=key2_value, width=80, anchor='w', wraplength=500, justify='left')
                        value.grid(row=i, column=1, padx=5, pady=5, sticky='nw')
                        i+=1
                else: 
                    label = tk.Label(description_window, text= key, width=40, anchor='w')
                    label.grid(row=i, column=0, padx=5, pady=5, sticky='nw')
                    value = tk.Label(description_window, text=key_value, width=80, anchor='w', wraplength=500, justify='left')
                    value.grid(row=i, column=1, padx=5, pady=5, sticky='nw')
                    i+=1
        
    ####################################################################################
                    
        def create_condition_window():
            condition_window = tk.Toplevel(new_window)
            condition_window.title("Conditions")

            i=0

            conditionmodule = full_studies['FullStudiesResponse']['FullStudies'][study_index]['Study']['ProtocolSection']['ConditionsModule']

            for key in conditionmodule:
                key_value = conditionmodule[key]
                if type(key_value) == dict:

                    for key2 in key_value:
                        key2_value = key_value[key2]
                        label = tk.Label(condition_window, text= key2, width=40, anchor='w')
                        label.grid(row=i, column=0, padx=5, pady=5)
                        value = tk.Label(condition_window, text=key2_value, width=80, anchor='w')
                        value.grid(row=i, column=1, padx=5, pady=5)
                        i+=1
                else: 
                    label = tk.Label(condition_window, text= key, width=40, anchor='w')
                    label.grid(row=i, column=0, padx=5, pady=5)
                    value = tk.Label(condition_window, text=key_value, width=80, anchor='w')
                    value.grid(row=i, column=1, padx=5, pady=5)
                    i+=1
        
    ####################################################################################
                    
        def create_design_window():
            design_window = tk.Toplevel(new_window)
            design_window.title("Design")

            i=0

            designmodule = full_studies['FullStudiesResponse']['FullStudies'][study_index]['Study']['ProtocolSection']['DesignModule']

            for key in designmodule:
                key_value = designmodule[key]
                if type(key_value) == dict:

                    for key2 in key_value:
                        key2_value = key_value[key2]
                        label = tk.Label(design_window, text= key2, width=40, anchor='w', wraplength=500, justify='left')
                        label.grid(row=i, column=0, padx=5, pady=5, sticky='nw')
                        value = tk.Label(design_window, text=key2_value, width=80, anchor='w', wraplength=500, justify='left')
                        value.grid(row=i, column=1, padx=5, pady=5, sticky='nw')
                        i+=1
                else: 
                    label = tk.Label(design_window, text= key, width=40, anchor='w', wraplength=500, justify='left')
                    label.grid(row=i, column=0, padx=5, pady=5, sticky='nw')
                    value = tk.Label(design_window, text=key_value, width=80, anchor='w', wraplength=500, justify='left')
                    value.grid(row=i, column=1, padx=5, pady=5, sticky='nw')
                    i+=1
        
    ####################################################################################
    
        def create_intervention_window():
            intervention_window = tk.Toplevel(new_window)
            intervention_window.title("Arms/Interventions")

            i=0

            armsmodule = full_studies['FullStudiesResponse']['FullStudies'][study_index]['Study']['ProtocolSection']['ArmsInterventionsModule']['ArmGroupList']['ArmGroup'][0]
            interventionmodule = full_studies['FullStudiesResponse']['FullStudies'][0]['Study']['ProtocolSection']['ArmsInterventionsModule']['InterventionList']['Intervention']

            for key in armsmodule:
                key_value = armsmodule[key]
                if type(key_value) == dict:

                    for key2 in key_value:
                        key2_value = key_value[key2]
                        label = tk.Label(intervention_window, text= key2, width=40, anchor='w', wraplength=500, justify='left')
                        label.grid(row=i, column=0, padx=5, pady=5, sticky='nw')
                        value = tk.Label(intervention_window, text=key2_value, width=80, anchor='w', wraplength=500, justify='left')
                        value.grid(row=i, column=1, padx=5, pady=5, sticky='nw')
                        i+=1
                else: 
                    label = tk.Label(intervention_window, text= key, width=40, anchor='w', wraplength=500, justify='left')
                    label.grid(row=i, column=0, padx=5, pady=5, sticky='nw')
                    value = tk.Label(intervention_window, text=key_value, width=80, anchor='w', wraplength=500, justify='left')
                    value.grid(row=i, column=1, padx=5, pady=5, sticky='nw')
                    i+=1

            for intervention in interventionmodule:
                for key, item in intervention.items():
                    label = tk.Label(intervention_window, text= key, width=40, anchor='w', wraplength=500, justify='left')
                    label.grid(row=i, column=0, padx=5, pady=5, sticky='nw')
                    value = tk.Label(intervention_window, text=item, width=80, anchor='w', wraplength=500, justify='left')
                    value.grid(row=i, column=1, padx=5, pady=5, sticky='nw')
                    i+=1

        
    ####################################################################################
                    
        def create_outcomes_window(): 
            outcome_window = tk.Toplevel(new_window)
            outcome_window.title("Outcomes")

            i=0

            outcomemodule = full_studies['FullStudiesResponse']['FullStudies'][study_index]['Study']['ProtocolSection']['OutcomesModule']

            full_studies['FullStudiesResponse']['FullStudies'][0]['Study']['ProtocolSection']['OutcomesModule']['PrimaryOutcomeList']['PrimaryOutcome'][0]

            for key, item in outcomemodule.items():
                for key2, item2 in item.items():
                        for item3 in item2: 
                            label = tk.Label(outcome_window, text= key2, width=40, anchor='w', wraplength=500, justify='left')
                            label.grid(row=i, column=0, padx=5, pady=5)
                            value = tk.Label(outcome_window, text=item3, width=80, anchor='w', wraplength=500, justify='left')
                            value.grid(row=i, column=1, padx=5, pady=5)
                            i+=1
                
    ####################################################################################

        def create_eligibility_window():
            eligibility_window = tk.Toplevel(new_window)
            eligibility_window.title("Eligibility")

            i=0

            eligibilitymodule = full_studies['FullStudiesResponse']['FullStudies'][study_index]['Study']['ProtocolSection']['EligibilityModule']

            for key in eligibilitymodule:

                key_value = eligibilitymodule[key]

                if type(key_value) == dict:

                    for key2 in key_value:
                        key2_value = key_value[key2]
                        label = tk.Label(eligibility_window, text= key2, width=40, anchor='w', wraplength=500, justify='left')
                        label.grid(row=i, column=0, padx=5, pady=5, sticky='nw')
                        value = tk.Label(eligibility_window, text=key2_value, width=80, anchor='w', wraplength=500, justify='left')
                        value.grid(row=i, column=1, padx=5, pady=5, sticky='nw')
                        i+=1
                else: 
                    label = tk.Label(eligibility_window, text= key, width=40, anchor='w', wraplength=500, justify='left')
                    label.grid(row=i, column=0, padx=5, pady=5, sticky='nw')
                    value = tk.Label(eligibility_window, text=key_value, width=80, anchor='w', wraplength=500, justify='left')
                    value.grid(row=i, column=1, padx=5, pady=5, sticky='nw')
                    i+=1
        
    ####################################################################################
    
        def create_location_window():
            location_window = tk.Toplevel(new_window)
            location_window.title("Contacts/Locations")

            i=0

            locationmodule = full_studies['FullStudiesResponse']['FullStudies'][study_index]['Study']['ProtocolSection']['ContactsLocationsModule']


            for key, item in locationmodule.items():
                for key2, item2 in item.items():
                        for key3, item3 in item2[0].items():
                            label = tk.Label(location_window, text= key3, width=40, anchor='w', wraplength=500, justify='left')
                            label.grid(row=i, column=0, padx=5, pady=5, sticky='nw')
                            value = tk.Label(location_window, text=item3, width=80, anchor='w', wraplength=500, justify='left')
                            value.grid(row=i, column=1, padx=5, pady=5, sticky='nw')
                            i+=1

        
    ####################################################################################
    
        def create_reference_window():
            reference_window = tk.Toplevel(new_window)
            reference_window.title("References")

            i=0

            referencemodule = full_studies['FullStudiesResponse']['FullStudies'][study_index]['Study']['ProtocolSection'].get('ReferencesModule', 'N/A')

            if type(referencemodule) != str:
                for key, item in referencemodule.items():
                    if item == dict:
                        for key2, item2 in item.items():
                                for key3, item3 in item2[0].items():
                                    label = tk.Label(reference_window, text= key3, width=40, anchor='w', wraplength=500, justify='left')
                                    label.grid(row=i, column=0, padx=5, pady=5, sticky='nw')
                                    value = tk.Label(reference_window, text=item3, width=80, anchor='w', wraplength=500, justify='left')
                                    value.grid(row=i, column=1, padx=5, pady=5, sticky='nw')
                                    i+=1
            else:
                label = tk.Label(reference_window, text= referencemodule, width=40, anchor='w', wraplength=500, justify='left')
                label.grid(row=0, column=0, padx=5, pady=5, sticky='nw')
        
    ####################################################################################
    
        def create_IPD_window():
            IPD_window = tk.Toplevel(new_window)
            IPD_window.title("IPD Sharing Statement")

            i=0

            IPDmodule = full_studies['FullStudiesResponse']['FullStudies'][study_index]['Study']['ProtocolSection'].get('IPDSharingStatementModule', 'N/A')

            
            if IPDmodule != str:
                for key, item in IPDmodule.items():
                    label = tk.Label(IPD_window, text= key, width=40, anchor='w')
                    label.grid(row=i, column=0, padx=5, pady=5)
                    value = tk.Label(IPD_window, text=item, width=80, anchor='w')
                    value.grid(row=i, column=1, padx=5, pady=5)
                    i+=1
            else:
                label = tk.Label(IPD_window, text= IPDmodule, width=40, anchor='w')
                label.grid(row=0, column=0, padx=5, pady=5)

        
    ####################################################################################
        
        status_button = tk.Button(new_window, text='Status', width=15, height=2, command= create_status_window)
        status_button.grid(row=0, column=0, padx=5, pady=5)

        sponsor_button = tk.Button(new_window, text='Collaborators/Sponsors', width=15, height=2, command= create_sponsor_window)
        sponsor_button.grid(row=0, column=1, padx=5, pady=5)
        
        oversight_button = tk.Button(new_window, text='Oversight', width=15, height=2, command= create_oversight_window)
        oversight_button.grid(row=0, column=2, padx=5, pady=5)

        description_button = tk.Button(new_window, text='Description', width=15, height=2, command= create_description_window)
        description_button.grid(row=0, column=3, padx=5, pady=5)

        condition_button = tk.Button(new_window, text='Conditions', width=15, height=2, command= create_condition_window)
        condition_button.grid(row=1, column=0, padx=5, pady=5)
        
        design_button = tk.Button(new_window, text='Design', width=15, height=2, command= create_design_window)
        design_button.grid(row=1, column=1, padx=5, pady=5)
        
        intervention_button = tk.Button(new_window, text='Arms/Intervention', width=15, height=2, command= create_intervention_window)
        intervention_button.grid(row=1, column=2, padx=5, pady=5)
        
        outcomes_button = tk.Button(new_window, text='Outcomes', width=15, height=2, command= create_outcomes_window)
        outcomes_button.grid(row=1, column=3, padx=5, pady=5)
        
        eligibility_button = tk.Button(new_window, text='Eligibility', width=15, height=2, command= create_eligibility_window)
        eligibility_button.grid(row=2, column=0, padx=5, pady=5)
        
        location_button = tk.Button(new_window, text='Locations', width=15, height=2, command= create_location_window)
        location_button.grid(row=2, column=1, padx=5, pady=5)
        
        reference_button = tk.Button(new_window, text='References', width=15, height=2, command= create_reference_window)
        reference_button.grid(row=2, column=2, padx=5, pady=5)
        
        IPD_button = tk.Button(new_window, text='IPD Sharing', width=15, height=2, command= create_IPD_window)
        IPD_button.grid(row=2, column=3, padx=5, pady=5)

        
    # Your existing code for creating input_frame, labels, entry fields, and trv goes here...

    def MouseButtonDoubleClickCallBack(event):
        currentRowIndex = trv.selection()[0]
        lastTuple = trv.item(currentRowIndex, 'values')
        study_index = trv.index(currentRowIndex)  
        open_new_window(lastTuple, study_index=study_index)

    trv.bind("<Double-1>", MouseButtonDoubleClickCallBack)  # Double-click event
    trv.bind("<ButtonRelease>",MouseButtonUpCallBack)

    load_trv_with_json()
    root.mainloop()

if __name__== "__main__":
    # Create the main window
    window = tk.Tk()
    window.title("Clinical Trial Search Tool")

    # Create labels and entry fields for name and age
    search_label = tk.Label(window, anchor="w", text="Please input search phrase:")
    search_label.grid(row=0, column=0, padx=10, pady=5)

    search_entry = tk.Entry(window, relief='ridge')
    search_entry.grid(row=0, column=1, padx=10, pady=5)

    count_label = tk.Label(window, anchor="w", text="Please input number of studies required:")
    count_label.grid(row=1, column=0, padx=10, pady=5)

    count_entry = tk.Entry(window, relief='ridge')
    count_entry.grid(row=1, column=1, padx=10, pady=5)

    # Create a submit button
    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Run the application
    window.mainloop()

