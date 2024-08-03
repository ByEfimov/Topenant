export enum ResponseStatus {
    success = 'success',
    error = 'error',
}

export interface ISuccessResponse<T> {
    status: ResponseStatus.success;
    data: T;
    errors: [];
}

export interface IError {
    message: string;
    code: number | string;
    customData: string;
}

export interface IErrorResponse {
    status: ResponseStatus.error;
    data: null;
    errors: IError[];
}

export type IResponse<T> = ISuccessResponse<T> | IErrorResponse;

export function instanceOfIErrorResponse(
    object: any
): object is IErrorResponse {
    return 'status' in object && 'data' in object && 'errors' in object;
}
