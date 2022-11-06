from datapackage import get_csv_headers

if __name__ == '__main__':
    # show_file_first_line("/home/jakub/PycharmProjects/ASI_pro_autoML/local_data/car_prices.csv")
    # show_csv_head("/home/jakub/PycharmProjects/ASI_pro_autoML/local_data/car_prices.csv")
    headers = get_csv_headers("/home/jakub/PycharmProjects/ASI_pro_autoML/local_data/car_prices.csv")
    print(headers)
