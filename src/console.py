from dashboardBuilder import DashboardBuilder

def main():
	"""
	This module contain the console of the APP	
	It implements the Main method
	@author : ahmed.bouzidia@ecoles-epsi.net
	"""
    dashboard_builder = DashboardBuilder()
    
    dashboard = dashboard_builder.build()
    
    dashboard.launchDashboard()

if __name__ == "__main__":
    main()
