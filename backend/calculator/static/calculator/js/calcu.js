const button = document.getElementById("but");
const area = document.getElementById("quantity");
const thickness = document.getElementById("thickness");
const price = document.getElementById("price");


button.addEventListener("click", () => {
    let data = {
        'required_area': area.value,
        'sheet_thickness': thickness.value,
        'package_price': price.value,
        'insulation': thickness.options[thickness.selectedIndex].text
    }
    console.log(data)
    async function calcu() {
        const response =  await fetch(
            'http://192.168.31.47/calculation',
            {
                method: 'POST',
                body: JSON.stringify(data),
                headers: {'Content-Type': 'application/json; charset=UTF-8',},
            }
        );
        const response_data = await response.json();
        console.log(response_data);
        document.getElementById("number_sheets").textContent = `Общее количество листов: ${response_data.number_sheets}`;
        document.getElementById("number_packages").textContent = `Общее количество упаковок: ${response_data.number_packages}`;
        document.getElementById("number_sheets_plus").textContent =`Дополнительных листов: ${ response_data.number_sheets_plus}`;
        document.getElementById("total_volume").textContent =`Общий объём: ${ response_data.total_volume} м3`;
        document.getElementById("total_price").textContent = `Итого цена: ${response_data.rubles} руб, ${response_data.pennies} коп`;
    }
    calcu()
});
