import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

export interface ShoppingCartState {
    value: number;
}

const initialState: ShoppingCartState = {
    value: 0
}

export const shoppingCartSlice = createSlice({
    name: "shoppingCart",
    initialState,
    reducers: {
        increment: (state) => {
            state.value += 1
        },
        decrement: (state) => {
            state.value -= 1
        },
        incrementByAmount: (state, action: PayloadAction<number>) => {
            state.value += action.payload
        }
    }
})


export const { increment, decrement, incrementByAmount } = shoppingCartSlice.actions
export default shoppingCartSlice.reducer