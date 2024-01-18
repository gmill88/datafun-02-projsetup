'''Start a data analytics project'''

import pathlib 


def create_project_directory(directory_name: str):
    """
    creates a project sub-directory
    :param directory_name
    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)

def create_annual_data_directories(directory_name: str, start_year: 2015, end_year: 2020):
   """
   Creates project sub-directory
   :param directory_name: Name to be created, e.g. "data"
   :param start: First year to be created, e.g. 2000
   :param end: Last year to be created, e.g. 2024
   """
   create_project_directory(directory_name)

   for year in range(start_year, end_year + 1):
      print(year)
      year_directory = pathlib.Path(directory_name).joinpath(str(year))
      print(year_directory)
      create_project_directory(year_directory)
      print(f"created{year_directory}")

def main():
   '''Scaffold Project'''
   create_project_directory(directory_name='test')
   create_project_directory(directory_name='docs')
   create_annual_data_directories(directory_name='data', start_year=2015, end_year=2020)



if __name__ == '__main__':
   main()