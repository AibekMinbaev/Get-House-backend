import "./Header.css"
import logo from "../static/logo_used.png" 

console.log(logo) 


export default function Header(){
    return(
        <div id="main-header">
            <div id="inner-header">
                <div id="header-left">
                    <img id="logo-img" alt="Logo" src={logo} href="/"/>
                </div> 

                <div id="header-middle">
                    <a className="header-routes" href="/buy">Buy</a>
                    <a className="header-routes" href="/rent">Rent</a>
                    <a className="header-routes" href="/sell">Sell</a>
                    <a className="header-routes" href="/agents">Find Agents</a>
                    <a className="header-routes" href="/aboutus">About Us</a>
                </div>

                <div id="header-right">
                    <button id="login-button">Login</button>
                </div>
            </div>
        </div>
    )
}