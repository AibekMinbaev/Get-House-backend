import React from 'react' 

class App extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: []
    };
  }

  componentDidMount() {
    fetch("http://localhost:8000/api/properties/")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({ 
            isLoaded: true,
            items: result
          });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }

  render() {
    const { error, isLoaded, items } = this.state;

    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <div id="main-div">
           <section id="info">
          <h1>The list of properties: </h1>
        </section> 
        <section id="property-list">
          <ul id="property_list">
            {items?.map(item => (
              <li>
                {item.title}:   {item.price}
              </li>
            ))}
          </ul>
        </section>
        </div>
      );
    }
  }
}

export default App;
