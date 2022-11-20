const selectCategory = document.getElementById('categories')

      selectCategory.addEventListener('change', ()=> {
        console.log(selectCategory.value)
        
        fetch(`/${selectCategory.value}`).then(response => response.json()).then(data => console.log(data))

        window.location.replace(`/${selectCategory.value}`)
        
      })