import React, { Component } from 'react';
import './App.css';

class App extends Component {
    state = { loading: false };

    componentDidMount() {
        // fetch('http://localhost:8000/api/listings');
        fetch('http://127.0.0.1:8000/api/listings/')
            .then(response => response.json())
            .then(data => this.setState({ items: data }));
    }

    render() {
        const { items } = this.state;
        return (
            <div id="bla">
                <h1>Welcome to main page</h1>
                {items.map(item => (
                    <div key={item.id}>
                        <h1>{item.title}</h1>
                        <p>{item.body}</p>
                    </div>
                ))}
            </div>
        );
    }
}

export default App;
