from data_analysis import data_analysis

def data_cleaning():
    data = data_analysis()
    
    columns_to_drop = ["emp_length", "state", "debt_to_income", "annual_income_joint", "verification_income_joint",
                       "debt_to_income_joint", "delinq_2y", "months_since_last_delinq", 'earliest_credit_line', 
                       'inquiries_last_12m', 'total_credit_lines', 'open_credit_lines', 'total_credit_limit', 
                       'total_credit_utilized', 'num_collections_last_12m', 'num_historical_failed_to_pay', 
                       'months_since_90d_late', 'current_accounts_delinq', 'total_collection_amount_ever', 
                       'current_installment_accounts', 'accounts_opened_24m', 'months_since_last_credit_inquiry', 
                       'num_satisfactory_accounts', 'num_accounts_120d_past_due', 'num_accounts_30d_past_due', 
                       'num_active_debit_accounts', 'total_debit_limit', 'num_total_cc_accounts', 'num_open_cc_accounts', 
                       'num_cc_carrying_balance', 'num_mort_accounts', 'account_never_delinq_percent', 'tax_liens', 
                       'public_record_bankrupt', 'grade', 'sub_grade','paid_principal', "application_type", 'initial_listing_status', 'disbursement_method']
    df = data.drop(columns=columns_to_drop, axis=1)
    print(df.dtypes)
    

    return df

data_cleaning()