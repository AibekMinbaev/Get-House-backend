import "./Property.css"

export default function Property({price, city, square_footage, num_bathrooms, num_bedrooms, property_image}){
    return (
        <div id="property-item">
            <div id="description">
                <p>{num_bedrooms} bedrooms, {num_bathrooms} bathrooms</p>
                <p>Price: {price}$</p>
                <p>City: {city}</p>
                <p>Square footage: {square_footage}</p>
            </div>
            <div id="images">
                 <img src={property_image}></img>
            </div>
        </div>
    )
} 
