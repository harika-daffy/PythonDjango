import {FETCH_POST , NEW_POST} from '../actions/actions';


const initialState={
    items:[],
    

}

export default function(state=initialState,action){
    switch (action.type){
        case FETCH_POST:
            return {
                ...state ,
            items: action.payload
        };
        
        default:
            return state
    }
}