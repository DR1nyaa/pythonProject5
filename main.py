import os


def merge_files(input_files, output_file):

    file_data = []


    for file_name in input_files:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                file_data.append({
                    'name': file_name,
                    'lines': lines,
                    'line_count': len(lines)
                })
        except FileNotFoundError:
            print(f"Файл {file_name} не найден.")


    file_data.sort(key=lambda x: x['line_count'])


    with open(output_file, 'w', encoding='utf-8') as output:
        for data in file_data:
            output.write(f"{data['name']}\n")
            output.write(f"{data['line_count']}\n")
            output.writelines(data['lines'])
            output.write("\n")  # Добавляем пустую строку между файлами

    print(f"Данные успешно объединены в файл {output_file}")



input_files = ['1.txt', '2.txt']
output_file = 'result.txt'
merge_files(input_files, output_file)
