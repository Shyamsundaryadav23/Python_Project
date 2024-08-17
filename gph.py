import matplotlib.pyplot as plt
def create_bar_chart(x_values, y_values):
    plt.bar(x_values, y_values,color='blue',width=0.4)
    plt.xlabel('X Values as Year in which Student Enrolled for Courses')
    plt.ylabel('Y Values as Count ')
    plt.title('Bar Chart Student Enrollment for Python Course')
    fig = plt.figure(figsize=(16, 8))
    plt.savefig('bar_chart.png') # Save the chart as an image file
    plt.show()
def main():
    x_values = []
    y_values = []

    n = int(input("Enter the number of data points: "))
    for i in range(n):
        x = float(input("Enter the x value: "))
        y = float(input("Enter the y value: "))
        x_values.append(x)
        y_values.append(y)
    create_bar_chart(x_values, y_values)
if __name__ == "__main__":
    main()