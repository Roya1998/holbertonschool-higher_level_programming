// Add click event listener to the element with id 'add_item'
document.querySelector("#add_item").addEventListener("click", function () {
  // Create a new li element
  const newItem = document.createElement("li");
  newItem.textContent = "Item";

  // Add the new li element to the ul with class 'my_list'
  document.querySelector(".my_list").appendChild(newItem);
});
