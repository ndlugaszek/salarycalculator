import argparse
import yaml
import functions.chartplot as cp
import functions.netsalarycalc as nsc


def salary_calculator():
    """Run the salary calculator which returns the gross salary connected to the net salary;
    Draw a bar chart that shows dependencies between the gross and the net salary"""
    salaries = get_arguments()
    net_salaries = nsc.get_net_salaries(salaries)
    salary_connections = zip(salaries, net_salaries)
    salary_connections = dict(salary_connections)
    print("Brutto: Netto")
    print(yaml.dump(salary_connections))
    possible_answers = ('t', 'n')
    user_answer = ''
    will_plot = ''
    while user_answer not in possible_answers:
        will_plot = input("Czy pokazac wykres? Wpisz 't' dla tak lub 'n' dla nie: ").lower()
        if will_plot in possible_answers:
            break
    if will_plot == 't':
        cp.draw_bar_chart(salaries, net_salaries)


def get_arguments():
    """Extract the cli arguments to the list"""
    parser = argparse.ArgumentParser(description='Salary calculator.')
    parser.add_argument('-L', '--nargs-int-type', nargs='*', type=int)
    for _, arguments in parser.parse_args()._get_kwargs():
        if arguments is not None:
            return arguments


if __name__ == '__main__':
    salary_calculator()
