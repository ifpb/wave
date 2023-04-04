// Selects the element with the "alert" class
 const alertElement = document.querySelector(".alert");
 function setAlert(){
  
// Sets the number of seconds that the alert should be visible
  const secondsToShow = 5;

// Defines a function to hide the alert after the set time
  const hideAlert = () => {
    alertElement.style.display = "none";
  };

 // Waits for the set time and then hides the alert
  setTimeout(hideAlert, secondsToShow * 1000);

}
if (alertElement !== null) {

  setAlert()
}