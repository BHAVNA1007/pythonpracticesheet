bill = []

def generate_bill():
    p_id = int(input("Enter Patient ID: "))
    c_charge = int(input("Enter Consultation Charges: "))
    m_cost = int(input("Enter Medicine Cost: "))
    t_charge = int(input("Enter Test Charges: "))

    gen_bill = {
       "Patient ID": p_id,
       "Consultation Charges":c_charge,
       "Medicine Cost": m_cost,
       "Test Charges": t_charge
    }
    bill.append(gen_bill)

    total = c_charge + m_cost + t_charge

    print("\nBill Details")
    for k , v in gen_bill.items():
        print(k ,":", v)

    print("Total Bill: ", total)  
       