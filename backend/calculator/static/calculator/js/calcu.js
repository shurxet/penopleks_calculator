const button = document.getElementById("but");
const area = document.getElementById("area");
const insulation = document.getElementById("insulation");
const price = document.getElementById("price");

button.addEventListener("click", () => {
    let data = {
        'id': Number(insulation.value),
        'area': Number(area.value),
        'price': Number(price.value),
        // 'insulation': insulation.options[insulation.selectedIndex].text
    }
    console.log(data)
    async function calcu() {
        const response =  await fetch(
            'http://localhost:8000/calculation',
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
