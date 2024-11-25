from applications.salary import calculate_salary
from applications.db.people import get_employes
from datetime import datetime as dt

def main():
  print(dt.now().date())
  print(calculate_salary())
  print(get_employes())


if __name__ == "__main__":
  main()