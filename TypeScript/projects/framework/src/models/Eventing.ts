type Callback = () => void; /*type alias for functions, makes code more readable*/

export class Eventing {
  events: {
    [key: string]: Callback[];
  } = {}; /*an object with event listeners and their callback functions*/

  /*function to add event listeners and callback functions to our user*/
  on = (eventName: string, callback: Callback): void => {
    const handlers = this.events[eventName] || [];
    handlers.push(callback);
    this.events[eventName] = handlers;
  };
  trigger = (eventName: string): void => {
    const handlers = this.events[eventName];
    /*if we have no handlers, stop*/
    if (!handlers || handlers.length === 0) {
      return;
    }
    /*otherwise call the handler functions*/
    handlers.forEach((callback) => {
      callback();
    });
  };
}
