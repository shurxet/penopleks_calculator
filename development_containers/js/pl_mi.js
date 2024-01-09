const bt_plus = document.getElementById("plus");
const bt_minus = document.getElementById("minus");
const quantity = document.getElementById("quantity");


bt_plus.addEventListener( "click", () => {
      const result = Number(quantity.value) + 1
      quantity.value = result
});

bt_minus.addEventListener( "click", () => {
      const result = Number(quantity.value)
      if (result == 0) {
          quantity.value = 0
      } else {
          quantity.value = result - 1
        }
});
