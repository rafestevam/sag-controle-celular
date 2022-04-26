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