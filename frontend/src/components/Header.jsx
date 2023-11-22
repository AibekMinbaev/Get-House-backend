import "./Header.css"
import logo from "../static/logo_used.png" 

console.log(logo) 


export default function Header(){
    return(
        <div id="main-header">
            <div id="inner-header">
                <div id="header-left">
                    <img id="logo-img" style={{height: 80}} alt="Logo" src={logo} href="/"/>
                </div> 

                <div id="header-middle">
                    <a className="header-routes">Buy</a>
                    <a className="header-routes">Rent</a>
                    <a className="header-routes">Sell</a>
                    <a className="header-routes">Find Agents</a>
                    <a className="header-routes">About Us</a>
                </div>

                <div id="header-right">
                    <button id="login-button">Login</button>
                </div>
            </div>
        </div>
    )
}