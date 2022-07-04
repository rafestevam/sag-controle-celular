export enum NotificationType {
    SUCCESS,
    WARNING,
    DANGER,
}
export default interface INotification {
    id: string,
    type: NotificationType,
    message: string,
}

export interface IModalNotification {
    title: string,
    message: string,
    modalType: NotificationType,
}