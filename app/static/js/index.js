
function setValueRangeNumber(idInRanger, idInNumber){

  document.getElementById(idInRanger).addEventListener("input", function () {
    document.getElementById(idInNumber).value = this.value;
  });

}

function setValueNumberRanger(idInNumber, idInRanger){

  document.getElementById(idInNumber).addEventListener("input", function () {
    document.getElementById(idInRanger).value = this.value;
  });

}
// Set Memory server
setValueRangeNumber("memoryserver", "memserverValue")
setValueNumberRanger("memserverValue","memoryserver")

// Set vcpu server
setValueRangeNumber("vcpuserver", "cpuserverValue")
setValueNumberRanger("cpuserverValue","vcpuserver")


// Set Memory client
setValueRangeNumber("memoryclient", "memclientValue")
setValueNumberRanger("memclientValue","memoryclient")

// Set vcpu client
setValueRangeNumber("vcpuclient", "cpuclientValue")
setValueNumberRanger("cpuclientValue","vcpuclient")


// Select Model

document.getElementById("model-select").addEventListener("change", function() {
  const modelsParms = ['sin', 'flashc'];

  modelsParms.forEach((valor) => {
    document.getElementById(valor).style.display = "none";
  });
  let selectedDiv = document.getElementById(this.value);
  if(selectedDiv){
    selectedDiv.style.display = "flex";
  }

});