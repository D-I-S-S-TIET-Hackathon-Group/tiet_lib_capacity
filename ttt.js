function nextpage() {
    // Navigate to the next page
    window.location.href = "ttt.html";
  }
  
  

function updateTime() {
    let now = new Date();
   let hours = String(now.getHours()).padStart(2, '0');
   let minutes = String(now.getMinutes()).padStart(2, '0');
   let seconds = String(now.getSeconds()).padStart(2, '0');
    document.getElementById('clock').innerText = hours +":"+minutes+":"+seconds;
  }
  
  // Update time every second
  setInterval(updateTime, 1000);
  
  // Initial call to display time immediately
  updateTime();

  