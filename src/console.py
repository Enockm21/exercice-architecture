from dashboardBuilder import DashboardBuilder

def main():
    dashboard_builder = DashboardBuilder()
    
    dashboard = dashboard_builder.build()
    
    dashboard.launchDashboard()

if __name__ == "__main__":
    main()
