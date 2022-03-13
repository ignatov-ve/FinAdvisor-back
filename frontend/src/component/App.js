import React from "react";
import Display from "./Display";
import ButtonPanel from "./ButtonPanel";
import calculate from "../logic/calculate";
import "./App.css";
import Popup from "./Popup"

const PI = 3.14;

export default class App extends React.Component {
    state = {
        total: null,
        next: null,
        operation: null,
        showPopup: false
    };

    openPopupHandler = () => {
        this.setState({showPopup: true});
    }

    closePopupHandler = () => {
        this.setState({showPopup: false});
    }

    handleClick = buttonName => {
        this.setState(calculate(this.state, buttonName));
        console.log('Open popup', this.state.total);
        if (this.state.next === PI.toString()) {
            this.openPopupHandler();
        }
    };

    render() {
        let popup = null;
        if (this.state.showPopup) {
            popup = (<Popup message='This is PI' closeMe={this.closePopupHandler}/>);
        }
        return (
            <div className="component-app">
                <Display value={this.state.next || this.state.total || "0"}/>
                <ButtonPanel clickHandler={this.handleClick}/>
                {popup}
            </div>
        );
    }
}
