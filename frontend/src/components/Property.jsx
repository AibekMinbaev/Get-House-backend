import "./Property.css"

export default function Property({price, city}){
    return (
        <div id="property-item">
            <p>Price: {price}$</p>
            <p>{city}</p>
        </div>
    )
} 
