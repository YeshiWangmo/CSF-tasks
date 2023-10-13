def calculate_area(length, width):
    return length * width
def calculate_perimeter(length, width):
    return 2 * (length + width)
def rectangle_info(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    print(f'Area of the rectangle: {area}')
    print(f'Perimeter of the rectangle: {perimeter}')
rectangle_info(4, 5)

