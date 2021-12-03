const gameForm = document.getElementById('game-form')

const gamesDataBox = document.getElementById('games-data-box')
const gameInput = document.getElementById('games')

const campsDataBox = document.getElementById('camps-data-box')
const campInput = document.getElementById('camps')

const btnBox = document.getElementById('btn-box')
const alertBox = document.getElementById('alert-box')

const campText = document.getElementById('camp-text')
const gameText = document.getElementById('game-text')


const csrf = document.getElementsByName('csrfmiddlewaretoken')



$.ajax({
    type: 'GET',
    url: '/games-json/',
    success: function(response){
        console.log(response.data)
        const gamesData = response.data
        gamesData.map(item=>{
            const option = document.createElement('div')
            option.textContent = item.name
            option.setAttribute('class', 'item')
            option.setAttribute('data-value', item.name)
            gamesDataBox.appendChild(option)
        })
    },
    error: function(error){
        console.log(error)
    }
})

gameInput.addEventListener('change', e=>{
    console.log(e.target.value)
    const selectedGame = e.target.value

    alertBox.innerHTML=""
    campsDataBox.innerHTML = ""
    campText.textContent = "Choose a camp"
    campText.classList.add("default")

    $.ajax({
        type: 'GET',
        url: `camps-json/${selectedGame}/`,
        success: function(response){
            console.log(response.data)
            const campsData = response.data
            campsData.map(item=>{
                const option = document.createElement('div')
                option.textContent = item.start_date + " - " + item.end_date
                option.setAttribute('class', 'item')
                option.setAttribute('data-value', item.start_date + " - " + item.end_date)
                campsDataBox.appendChild(option)
            })

            campInput.addEventListener('change', e=>{
                btnBox.classList.remove('not-visible')})
        },
        error: function(error){
            console.log(error)
        }
    })
})


gameForm.addEventListener('submit', e=>{
    e.preventDefault()
    console.log('submitted')

})
