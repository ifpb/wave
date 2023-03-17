
  const provisionUp = document.getElementById("provision-up");
  
  const provisionLoading = document.getElementById('provision-loading');

  provisionUp.addEventListener('click', () => {
      provisionUp.style.display = 'none';
      provisionLoading.style.display = 'inline-block';
    });

