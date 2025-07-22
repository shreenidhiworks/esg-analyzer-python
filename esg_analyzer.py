import pandas as pd

class ESGAnalyzer:
    def __init__(self, file_path):
        """Load the dataset."""
        self.df = pd.read_csv(file_path)
    
    def get_esg_info(self, company_name):
        """Retrieve ESG details for a given company name."""
        company_data = self.df[self.df['Name'].str.lower() == company_name.lower()]
        
        if company_data.empty:
            return "Company not found in the dataset. Please check the spelling."
        
        grade = company_data['Total_grade'].values[0]
        score = company_data['Total_score'].values[0]
        level = company_data['Total_level'].values[0]
        
        
        if score >= 1100:
            insight = "Excellent ESG performance! The company is a sustainability leader."
        elif 900 <= score < 1100:
            insight = "Good ESG performance. Some areas can still improve."
        elif 700 <= score < 900:
            insight = "Moderate ESG performance. The company needs to work on sustainability."
        else:
            insight = "Poor ESG performance. Significant improvement is needed."
        
        return (f"Company: {company_name}\n"
                f"ESG Grade: {grade}\n"
                f"ESG Score: {score}\n"
                f"ESG Level: {level}\n"
                f"Insight: {insight}")


if __name__ == "__main__":
    file_path = "new dataset for python.csv"  
    esg_analyzer = ESGAnalyzer(file_path)
    
    
    company_name = input("Enter a company name: ")
    print(esg_analyzer.get_esg_info(company_name))