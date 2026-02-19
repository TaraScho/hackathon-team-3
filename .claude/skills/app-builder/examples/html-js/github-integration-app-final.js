// For reference only. This demo app lives in https://github.com/DataDog/app-builder-roamlist
const itinerary = [];

function addDestination(destination, date, activities, restaurants) {
    itinerary.push({ destination, date, activities, restaurants });
    updateItineraryDisplay();
}

function removeDestination(index) {
    itinerary.splice(index, 1);
    updateItineraryDisplay();
}

function updateItineraryDisplay() {
    const itineraryList = document.getElementById('list');
    itineraryList.innerHTML = '';
    itinerary.forEach((item, index) => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<strong>Destination:</strong> ${item.destination} <br> <strong>Date:</strong> ${item.date} <br> <strong>Activities:</strong> ${item.activities} <br> <strong>Restaurants:</strong> ${item.restaurants}`;
        const removeButton = document.createElement('button');
        removeButton.textContent = 'Remove';
        removeButton.onclick = () => removeDestination(index);
        listItem.appendChild(removeButton);
        itineraryList.appendChild(listItem);
    });
}

document.getElementById('form').onsubmit = function(event) {
    event.preventDefault();
    const destinationInput = document.getElementById('destination');
    const dateInput = document.getElementById('date');
    const activitiesInput = document.getElementById('activities');
    const restaurantsInput = document.getElementById('restaurants');
    const destination = destinationInput.value.trim();
    const date = dateInput.value.trim();
    const activities = activitiesInput.value.trim();
    const restaurants = restaurantsInput.value.trim();
    if (destination && date && activities && restaurants) {
        addDestination(destination, date, activities, restaurants);
        destinationInput.value = '';
        dateInput.value = '';
        activitiesInput.value = '';
        restaurantsInput.value = '';
    }
};

